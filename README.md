#To activate venv 
.\env\Scripts\activate 

#To test:  
python -m pytest backend/tests

#To run:
 python -m backend.blockchain.blockchain

#TO START FROM SCRATCH

#To create virtual env
py -m pip install --user virtualenv
py -m venv env
.\env\Scripts\activate 

#To install dependencies from file 
pip install --user --requirement requirements.txt
 
#To install only a single package 
python -m pip install -U pytest