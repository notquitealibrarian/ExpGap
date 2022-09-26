# ExpGap
Python script to identify gaps in experience

# Description
ExpGap works by analying a JSON file representing the professional record of a Doctor in order to find gaps in experience of more than 31 days.  If a gap (or multiple gaps) are found, the console will output the dates that represent the gap.

# Running the script
Running the script is as as simple as running any python file.  The accompanying records.JSON must be located in the same directory as the script.  This file can be updated/replaced as needed.

# records.JSON format
The records in the JSON file follow the following format:
```
       { "f_name": "First Name",
          "l_name": "Last Name",
          "organization": "Organization Name",
          "start_date": "YYYY-MM-DD",
          "end_date": "YYYY-MM-DD" }
```

# Under the hood
The script works by first opening up the records file and accessing the data.  It then sorts the records by start date.  From there, it removes records that have an end date previous to the end date of the record before it.  Finally, it looks at this new list of records and checks the end date of the current record and the start date of the next record, and saves these dates in a list of tuples if there is a gap of more than 31 days between them.

# Author
Brett Edmonds
brett.g.edmonds@gmail.com
