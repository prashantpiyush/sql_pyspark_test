Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)
SensorSchedule = SensorSchedule(enabled = False)

with DAG(Schedule = Schedule, SensorSchedule = SensorSchedule):
    Reformat_with_random_id = Task(
        task_id = "Reformat_with_random_id", 
        component = "Reformat", 
        columnsSelector = [         "uwvXiRn5PXV2jzbEs0oN7$$OEtu0nw9b6eJrQ5iamKt6##id",          "uwvXiRn5PXV2jzbEs0oN7$$OEtu0nw9b6eJrQ5iamKt6##name",          "uwvXiRn5PXV2jzbEs0oN7$$OEtu0nw9b6eJrQ5iamKt6##department",          "uwvXiRn5PXV2jzbEs0oN7$$OEtu0nw9b6eJrQ5iamKt6##salary",          "uwvXiRn5PXV2jzbEs0oN7$$OEtu0nw9b6eJrQ5iamKt6##join_date"], 
        expressions = [{"expression" : {"expression" : "id"}, "alias" : "id", "_row_id" : "983160381"},          {"expression" : {"expression" : "name"}, "alias" : "full_name", "_row_id" : "197373482"},          {"expression" : {"expression" : "department"}, "alias" : "department", "_row_id" : "758547189"},          {"expression" : {"expression" : "salary"}, "alias" : "salary", "_row_id" : "233325642"},          {"expression" : {"expression" : "join_date"}, "alias" : "doj", "_row_id" : "1117863213"},          {"expression" : {"expression" : "43.2"}, "alias" : "random_id", "_row_id" : "pT0fT2YIU0"}]
    )
    new_reformat = Task(task_id = "new_reformat", component = "Reformat", columnsSelector = [], expressions = [])
    Reformat_1 = Task(task_id = "Reformat_1", component = "Reformat", columnsSelector = [], expressions = [])
    employee_records = Task(
        task_id = "employee_records", 
        component = "Dataset", 
        table = {"name" : "employees", "sourceType" : "Source", "sourceName" : "tanmay.piyush_test", "alias" : ""}, 
        writeOptions = {"writeMode" : "overwrite"}
    )
    employee_records.out >> Reformat_1.in0
    Reformat_1.out >> [Reformat_with_random_id.in0, new_reformat.in0]
