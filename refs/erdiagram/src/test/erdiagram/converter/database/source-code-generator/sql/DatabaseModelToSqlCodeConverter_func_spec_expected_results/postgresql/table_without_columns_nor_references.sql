CREATE TABLE "test_table" (
    "id" BIGINT NOT NULL GENERATED ALWAYS AS IDENTITY,
    CONSTRAINT "test_table_pk" PRIMARY KEY ("id")
);