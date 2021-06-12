# ipl-score-prediction-using-ML
Algorithm for 'main.py' file

1)Download the necessary libraries
2)Dowload the dataset using pandas

DATA PROCESS

  1) Keep the necessary columns 
  (eg:'match_id','venue','innings','ball','batting_team','bowling_team','striker','bowler','runs_off_bat','extras','wides',
        'noballs','byes','legbyes','penalty')
 and remove other columns.
 
  2) Calculate the total runs(total run=runs of bat+extras)
  3) Add a column named "total_runs" and drop the columns named-"runs_off_bat" and "extras"
  4) Next select rows only belonging to first 6 overs and innings less than 3
  5) Preprocess the data so that we get a tuple of following kind in each row:
  ('match_id','venue','innings','batting_team','bowling_team','total_runs')
  
  6) Convert back to dataframe
  7) Drop the column-'match_id'
  
  8) Keep only current teams 
  9) Remove other teams that is not playing in this IPL(2021)
  10) Perform 'label encoding' (replace the 'string' variable into 'integers') over 'venue','batting_team','bowling_team'
  
MODEL BUILDING

  11) Convert pandas data_frame into numpy array
  12) Separate input and output variables
  13) Split the  data into training set and testing set
  14) Convert it into tensor object and normalize the input data
  
  15) Built a neural network with one output layer 
  16) Train it with 'train dataset'
  17 )Evaluate the model with test dataset

MODEL SAVING
  
  18)Save the trained model
  20)Save the label encoders
  
  
