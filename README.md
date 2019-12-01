#To test:  
.\env\Scripts\python.exe -m pytest backend/tests

#To run:
 .\env\Scripts\python.exe -m backend.blockchain.blockchain

#To create virtual env
py -m pip install --user virtualenv
py -m venv env
.\env\Scripts\activate  

#To install 1 package 
.\env\Scripts\python.exe -m pip install -U pytest

#To install dependencies from file 
pip install --user --requirement requirements.txt