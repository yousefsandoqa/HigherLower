Install npm (https://www.npmjs.com/) and Python (https://www.python.org/) if you do not have them already.

## Clone the repo by running:

- git clone https://github.com/yousefsandoqa/HigherLower.git

## Database Setup in pgAdmin 4

- Create a new database, we recommend naming it CSE412Project

# Note: If you use a different name, you will need to edit database/db.py

## Remember which user you created the database under.

- Enter the query tool and run the schema.sql (copy and paste into the query tool)
- If this is the first setup, you will receive notices about tables not existing, you can ignore this.

## In the Default Workspace of pgAdmin4

- Go to Servers → PostgresQL 17 → Databases → CSE412Project, Refresh
- Then navigate to Schemas → Tables and use pgAdmin to populate the data in the following order. For each import, in options, set the delimiter to [comma] and enable Header. The CSVs listed below can be found in src/data
- Import player-final.csv to player
- Import teams.csv to team
- Import player_season-final.csv to player-season
- Import accolades.csv to accolades
- Import weighted-avgs.csv to career_stats

# Now, return to the software that will be running the code (we used VSCode)

- In src/server/database/db.py, update the dbname, user, and password if they differ from your local machine.

## In the directory HigherLower/my-react-app

- Run ‘npm install’

## In HigherLower/my-react-app/src/server

- Run ‘pip install -r requirements.txt’
- Launch the web app and API server
- Note: For this step, you will need to use two separate terminals

## In HigherLower/my-react-app/src/

- Run ‘uvicorn server.api.main:app --reload’

## In HigherLower/my-react-app

- Run ‘npm run dev’ and navigate to Local: http://localhost:[PORT] given in the terminal
