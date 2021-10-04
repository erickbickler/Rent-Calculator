# Rent Calculator

This program adjusts rent expenses for roommates where bills need to be split between people. It does this by subtracting the amount of the bill from the one who paid and splitting the expense between all the roommates that apply.

Reads from a json document called expenses.json and writes logs to monthlydata.json

Writes to a MongoDB Atlas Cluster

To connect to your own instance, create a file named .env with a line structured as:

`CONNECTION_STRING = "your_connection_string"`

It will write each month as a document in a collection called monthly_data in a db called rent

To run the program run:
`python rent.py`

To run in debug mode run:
`python rent.py True`