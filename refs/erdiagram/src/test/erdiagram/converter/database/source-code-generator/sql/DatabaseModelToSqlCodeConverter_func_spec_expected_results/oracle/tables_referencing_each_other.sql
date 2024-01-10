CREATE SEQUENCE "TEST_TABLE_1_SEQ" START WITH 1;
CREATE TABLE "TEST_TABLE_1" (
    "ID" NUMBER NOT NULL DEFAULT "TEST_TABLE_1_SEQ".nextval,
    "TABLE_2_ID" NUMBER NOT NULL,
    CONSTRAINT "TEST_TABLE_1_PK" PRIMARY KEY ("ID")
);

CREATE SEQUENCE "TEST_TABLE_2_SEQ" START WITH 1;
CREATE TABLE "TEST_TABLE_2" (
    "ID" NUMBER NOT NULL DEFAULT "TEST_TABLE_2_SEQ".nextval,
    "TABLE_1_ID" NUMBER NOT NULL,
    CONSTRAINT "TEST_TABLE_2_PK" PRIMARY KEY ("ID")
);

ALTER TABLE "TEST_TABLE_1" ADD CONSTRAINT "TEST_TABLE_1_TABLE_2_ID_FK" FOREIGN KEY ("TABLE_2_ID") REFERENCES "TEST_TABLE_2" ("ID");

ALTER TABLE "TEST_TABLE_2" ADD CONSTRAINT "TEST_TABLE_2_TABLE_1_ID_FK" FOREIGN KEY ("TABLE_1_ID") REFERENCES "TEST_TABLE_1" ("ID");