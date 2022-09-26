from datetime import datetime, timedelta
import json

with open('records.json', 'r') as openfile:
 
    # Reading from json file
    records = json.load(openfile)

# Function to sort the records based on the start date.  Could be modified to take
# an argument to stipulate the attribute to sort on.
def sort_records(records):
    sorted_records = sorted(
        records, key=lambda x: datetime.strptime(x["start_date"], "%Y-%m-%d")
        )
    return sorted_records

# Function to identify records in which a job is ended before the job
# directly previous to it has ended and remove them from the record list to test.
def remove_extra_records(records):
    # Uses the enumerate function in order to access the loop's index.
    for i, record in enumerate(records):
        # Only want to check the next record's start date if it exists (i.e. if
        # we're not looking at the last record in the list).
        if i+1 < len(records):
            end_date = datetime.strptime(record["end_date"], "%Y-%m-%d")
            next_record = sorted_records[i+1]
            next_end_date = datetime.strptime(next_record["end_date"], "%Y-%m-%d")
            # Checks to see if the next job in the list ends before the current job
            # and if so, removes from the list.
            if next_end_date < end_date:
                records.pop(i+1)
                # If the next record is removed, sets index back by one, so that when
                # i is incremented at end of loop, will compare next record to current
                i -= i
    return records

# Function to determine when/if a gap exists in records.  Note, records must be sorted,
# and if there are records in which a job is ended before the job directly previous
# to it has ended, the identified records must be removed from list.
def report_gaps(records):
    # Empty list to add identified gaps onto
    gaps = []
    for i, record in enumerate(records):
        if i+1 < len(records):
            end_date = datetime.strptime(record["end_date"], "%Y-%m-%d")
            next_record = records[i+1]
            next_start_date = datetime.strptime(next_record["start_date"], "%Y-%m-%d")
            next_end_date = datetime.strptime(next_record["end_date"], "%Y-%m-%d")
            # Checks to see if the next start date is within 31 days of the current
            # end date.
            if (end_date + timedelta(days=31)) < next_start_date:
                # if gap is found, add tuple of two dates to list
                gaps.append((end_date, next_start_date))
    # Return the list of gaps.  An empty list would mean no gaps were found.
    return gaps

# Sorts, removes "extra" records, and generates a list of gaps in employment (if any):
sorted_records = sort_records(records)
modified_records = remove_extra_records(sorted_records)
gap_list = report_gaps(modified_records)

#Print results to the screen
if not gap_list:
    print("No gaps in employment were found.  Hooray!")
else:
    for gaps in gap_list:
        first_date = gaps[0].strftime("%Y-%m-%d")
        second_date = gaps[1].strftime("%Y-%m-%d")
        print("There is a gap of more than 31 days between", first_date, "and", second_date)
