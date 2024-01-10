import moment, { locale } from 'moment-timezone'
import { translateTerritory, translateExemplarCity } from './Cldr'
// import { getActiveLocale } from './Locale'

function toDisplayName (name: string): string {
  return name.replace(/_/g, ' ')
}

interface TimezoneLocalizedData {
  group: string,
  locality: string,
  displayName: string
}
export class Timezone {
  readonly id: string
  private readonly territoryId: string
  private readonly exemplarCityId: string
  private readonly localizations: {[localeId: string]: TimezoneLocalizedData}
  constructor (id: string) {
    this.id = id
    const p = id.indexOf('/')
    if (p < 0) {
      this.territoryId = ''
      this.exemplarCityId = id
    } else {
      this.territoryId = id.substr(0, p)
      this.exemplarCityId = id.substr(p + 1)
    }
    this.localizations = {}
  }
  private get localization (): TimezoneLocalizedData {
    const localeId = 'en-US'
    if (!(localeId in this.localizations)) {
      const group = this.territoryId === '' ? 'others' : translateTerritory(this.territoryId, localeId)
      const locality = translateExemplarCity(this.exemplarCityId, localeId)
      if (!locality) {
        translateExemplarCity(this.exemplarCityId, localeId)
      }
      this.localizations[localeId] = {
        group,
        locality,
        displayName: this.territoryId === '' ? locality : `${group} - ${locality}`
      }
    }
    return this.localizations[localeId]
  }
  public get group (): string {
    return this.localization.group
  }
  public get locality () : string {
    return this.localization.locality
  }
  public get displayName () : string {
    return this.localization.displayName
  }
}

const map : { [id: string] : Timezone} = {}

const all: Timezone[] = []
function addUtcTimeZones() {
  // Moment.js uses the IANA timezone database, which supports generic time zones like 'Etc/GMT+1'.
  // However, the signs for these time zones are inverted compared to ISO 8601.
  // For more details, see https://github.com/moment/moment-timezone/issues/167
  for (let offset = -12; offset <= 12; offset++) {
    const posixSign = offset <= 0 ? '+' : '-';
    const isoSign = offset >= 0 ? '+' : '-';
    const link = `Etc/GMT${posixSign}${Math.abs(offset)}|UTC/GMT${isoSign}${Math.abs(offset)}`;
    moment.tz.link(link);
  }
}
addUtcTimeZones()
const ids: string[] = moment.tz.names()
ids.forEach((id) => {
  const timezone = new Timezone(id)
  all.push(timezone)
  map[id] = timezone
})

export function isValid (timezone: any): boolean {
  return typeof timezone === 'string' && timezone !== '' && map.hasOwnProperty(timezone)
}

export function getByID (timezone: any): Timezone|null {
  return isValid(timezone) ? map[timezone] : null
}

export function getGroups (): string[] {
  const groups: string[] = []
  all.forEach((timezone: Timezone): void => {
    if (groups.indexOf(timezone.group) < 0) {
      groups.push(timezone.group)
    }
  })
  groups.sort()
  return groups
}

export function getGroupedTimezones (): { [group: string] : Timezone[]} {
  const result: { [group: string] : Timezone[]} = {}
  all.forEach((timezone: Timezone): void => {
    if (timezone.group in result) {
      result[timezone.group].push(timezone)
    } else {
      result[timezone.group] = [timezone]
    }
  })
  Object.keys(result).forEach((group: string): void => {
    result[group].sort((a: Timezone, b: Timezone): number => {
      const na = a.locality.toLocaleLowerCase()
      const nb = b.locality.toLocaleLowerCase()
      if (na < nb) {
        return -1
      }
      if (na > nb) {
        return 1
      }
      return 0
    })
  })
  return result
}

export const MY_TIMEZONE: string = moment.tz.guess()
