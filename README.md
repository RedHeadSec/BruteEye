# BruteEye
A tool for brute forcing MotionEye camera web panels. The purpose of this tool is to address the issue of how MotionEye handles logins. While the login panel uses a normal POST request for username and password, it will always return a 200 with no real reliable way to tell a successful login versus a failed one as it also doesn't throw redirects. Instead, client side Javascript computes a epoch timestamp and a signature of several parameters within the request into a SHA1 hash. A new GET request is then sent which the server uses to return a 200 or 403. 


**Valid Pass:**
![Burp_Suite_Professional_v2022_11_3_-_Temporary_Project_-_licensed_to_Optiv_Secuirty__125_user_license_](https://user-images.githubusercontent.com/42355245/205472935-27a3f1f1-83eb-46b0-aac7-853dd941d2f2.png)
**Wrong Pass:**

![Burp_Suite_Professional_v2022_11_3_-_Temporary_Project_-_licensed_to_Optiv_Secuirty__125_user_license_](https://user-images.githubusercontent.com/42355245/205473029-94015c89-bfad-4a9a-8c6a-fe08a68df0bb.png)

**Following Successful GET Request:**
![Burp_Suite_Professional_v2022_11_3_-_Temporary_Project_-_licensed_to_Optiv_Secuirty__125_user_license__and_Editing_BruteEye_README_md_at_main_·_RedHeadSec_BruteEye](https://user-images.githubusercontent.com/42355245/205473116-3d62684c-c9bc-409a-ad83-1fc1c5116103.png)

**Failure:**
![Burp_Suite_Professional_v2022_11_3_-_Temporary_Project_-_licensed_to_Optiv_Secuirty__125_user_license_](https://user-images.githubusercontent.com/42355245/205473142-b4f37cf9-9544-4263-acd5-2a2b2ea212cf.png)

**Version 0.42:**
The configuration file hides the admin password, but the valid password is still found due to the configuration being dumped.

![Parrot_OS](https://user-images.githubusercontent.com/42355245/206356899-5d6c6b48-b067-4ce9-a75a-2ead58b32c32.png)




## Usage
```
 ____             _       _____              __   ___   __
| __ ) _ __ _   _| |_ ___| ____|   _  ___   / /  / _ \  \ \
|  _ \| '__| | | | __/ _ \  _|| | | |/ _ \ | |  | | | |  | |
| |_) | |  | |_| | ||  __/ |__| |_| |  __/ | |  | |_| |  | |
|____/|_|   \__,_|\__\___|_____\__, |\___| | |   \___/   | |
                               |___/        \_\         /_/

Author: Evasive_Ginger/RedHeadSec

usage: BruteEye.py [-h] [-p PORT] [-d DELAY] target password_list

A tool for brute forcing MotionEye camera web panels.

positional arguments:
  target                Enter the target host. EX: http://192.168.254.149:8765
  password_list         Enter the path for the password list.

optional arguments:
  -h, --help            show this help message and exit
  -p PORT, --port PORT  Port running MotoionEye web console.
  -d DELAY, --delay DELAY
                        Apply sleep limiting for X seconds/ms. Example: 0.5
```

## Showcase
![Parrot_OS_](https://user-images.githubusercontent.com/42355245/205472771-5abe4a7e-020b-4f80-a73a-7ea2f6709333.png)

## Questions/Comments
This is a pretty thrown together script for instances I find this service exposed. It may have bugs with edge cases and I have not implemented everything you may find, such as HTTPS endpoints. If you have problems or improvements, submit a pull or issue. Use only on assets you own or are allowed to perform testing on. Author holds no responsibilty for modification or misuse by third parties. 
