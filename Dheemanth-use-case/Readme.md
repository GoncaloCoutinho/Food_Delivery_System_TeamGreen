# Customer Review Feedback Use Case
In this use case I'm getting the customer review on their order when their order is confirmed
and sending notification to restaurant manager and driver.

## Details
When the Order is confirmed the customer gets an email with the feedback link.
The feedback link connects to the local server hosted and updates the MongoDB database collection called CustomerfeedbackComments.
As soon as a feedback for the order is registered in the database ,  two triggers are activated to send notification to restaurant
manager and the delivery driver.
