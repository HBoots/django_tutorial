# MVC vs. MVT

##

## Model-View-Controller

The MVC Software Architecture pattern.

Model

- data and logic
- interacts with database
- retreives data
- does NOT interact with View

View

- handles data presentation for the client
- does NOT interact with Model

Controller

- handles request
- communicates with Model for data
- communicates with View for client presentation
- handles response
- delivers response to client

## Model-View-Template

In the MVT pattern the View handles much of the work the Controller does in the MVC pattern while the Template handles much of the work the View does in the MVC pattern.

The typical style of MVT is to contain most of the business logic in the Model instead of the View (Fat Models, Skinny Views). Although often buisness logic is kept separately.

Model

- connects to the database

Template

- handles presentation for the client

View

- Handles request through url patterns
- communitates with Model for data
- communicates with Template for client presentation
- handles response
- delivers response to client through url patterns
