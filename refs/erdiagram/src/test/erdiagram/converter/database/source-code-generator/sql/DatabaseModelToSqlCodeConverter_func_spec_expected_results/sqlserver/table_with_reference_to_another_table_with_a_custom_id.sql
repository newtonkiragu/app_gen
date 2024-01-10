CREATE TABLE "TestTable1" (
    "Id" BIGINT NOT NULL IDENTITY(1, 1),
    "Table2Id" BIGINT NOT NULL,
    CONSTRAINT "TestTable1_pk" PRIMARY KEY ("Id")
);

CREATE TABLE "TestTable2" (
    "CustomId" BIGINT NOT NULL IDENTITY(1, 1),
    CONSTRAINT "TestTable2_pk" PRIMARY KEY ("CustomId")
);

ALTER TABLE "TestTable1" ADD CONSTRAINT "TestTable1_Table2Id_fk" FOREIGN KEY ("Table2Id") REFERENCES "TestTable2" ("CustomId");