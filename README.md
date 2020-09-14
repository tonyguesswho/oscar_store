# oscar_store
Adding registration endpoint to django-oscar-api




## Set Up Development With Docker


To setup for development with Docker after cloning the repository please do/run the following commands in the order stated below:

-   `cd <project dir>` to check into the dir
-   `docker-compose build`
-   `docker-compose up -d` to start the api after the previous command is successful

The `docker-compose build` command builds the docker image where the api and its postgres database would be situated.
Also this command does the necessary setup that is needed for the API to connect to the database.


To stop the running containers run the command `docker-compose down`




## API Endpoints
<table>
  <tr>
      <th>Request</th>
      <th>End Point</th>
      <th>Action</th>
  </tr>
    <tr>
      <td>POST</td>
      <td>/api/register/</td>
      <td>Register a User</td>
  </tr>
  <tr>
    <td>GET</td>
    <td>/api/register</td>
    <td>Get all registered users</td>
  </tr>

</table>


## Reistration fields

-email
-first_name
-last_name
-password