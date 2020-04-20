# Get-KFC
##### Automated KFC chicken bucket order via [WOLT](https://wolt.com/lt/discovery). 

Default order: 1 × Crispy stick bucket for four, 15 pcs.

![alt text](https://github.com/pijus-r/Get-KFC/blob/master/screen.png?raw=true)


 Requirements:
  - Python 3 
  - Selenium and Webdriver (Chrome was used in this instance)
  - colorama
  - pyfiglet
  
 Installation

 ```sh
 git clone https://github.com/pijus-r/Get-KFC.git
 cd Get-KFC
 sudo pip3 install selenium colorama pyfiglet
 # Uncomment to make an actual order (line 77): 'orderGo.click()'
 python3 bucket.py
 # or 'python bucket.py' if Python version 3 is your default 
```

### Todos

 - Launch code via command (anywhere from computer)
 - Easy install 
 - Handle login failure
 - ~~Ability to login without directly changing the code ~~
 - Change delivery address 
 - Select specific chicken bucket and extras
