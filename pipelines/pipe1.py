Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)
SensorSchedule = SensorSchedule(enabled = False)

with DAG(Schedule = Schedule, SensorSchedule = SensorSchedule):
    new_reformat = Task(task_id = "new_reformat", component = "Reformat", columnsSelector = [], expressions = [])
    Reformat_1 = Task(task_id = "Reformat_1", component = "Reformat", columnsSelector = [], expressions = [])
    employee_records = Task(
        task_id = "employee_records", 
        component = "Dataset", 
        table = {"name" : "employees", "sourceType" : "Source", "sourceName" : "tanmay.piyush_test", "alias" : ""}, 
        writeOptions = {"writeMode" : "overwrite"}
    )
    employee_records.out >> Reformat_1.in0
    Reformat_1.out >> new_reformat.in0
