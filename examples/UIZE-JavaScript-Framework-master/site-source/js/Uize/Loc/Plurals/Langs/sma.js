/*______________
|       ______  |   U I Z E    J A V A S C R I P T    F R A M E W O R K
|     /      /  |   ---------------------------------------------------
|    /    O /   |    MODULE : Uize.Loc.Plurals.Langs.sma Package
|   /    / /    |
|  /    / /  /| |    ONLINE : http://www.uize.com
| /____/ /__/_| | COPYRIGHT : (c)2015-2016 UIZE
|          /___ |   LICENSE : Available under MIT License or GNU General Public License
|_______________|             http://www.uize.com/license.html
*/

/* Module Meta Data
	type: Package
	importance: 1
	codeCompleteness: 100
	docCompleteness: 100
*/

/*?
	Introduction
		The =Uize.Loc.Plurals.Langs.sma= module implements a feature for determining a plural category from a number value for the sma language.

		*DEVELOPERS:* `Chris van Rensburg`

		Plural Categories
			........................................................
			<< table >>

			title: Plural Categories
			data:
			:| Category | Rule |
			:| one | n = 1 @integer 1 @decimal 1.0, 1.00, 1.000, 1.0000 |
			:| two | n = 2 @integer 2 @decimal 2.0, 2.00, 2.000, 2.0000 |
			:| other |  @integer 0, 3~17, 100, 1000, 10000, 100000, 1000000, … @decimal 0.0~0.9, 1.1~1.6, 10.0, 100.0, 1000.0, 10000.0, 100000.0, 1000000.0, … |
			........................................................
*/

Uize.module ({
	name:'Uize.Loc.Plurals.Langs.sma',
	required:'Uize.Loc.Plurals.Util',
	builder:function () {
		'use strict';

		return Uize.package ({
			getPluralCategory:function (_value) {
				return Uize.Loc.Plurals.Util.getPluralCategory (
					_value,
					function (n,i,f,t,v,w,within) {
						return n == 1 ? 'one' : n == 2 ? 'two' : 'other';
					}
				);
			}
		});
	}
});

