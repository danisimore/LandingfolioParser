# LandingfolioParser :gear:
![LandingfolioParser Logo](https://i.imgur.com/GTdaAzt.jpg)  
The parser that collects from the site [landingfolio.com](https://landingfolio.com) data about templates

## What data is being collected? :card_file_box:
**Collected data**:  
&nbsp;&nbsp;&nbsp;&nbsp;:white_check_mark: Template title;  
&nbsp;&nbsp;&nbsp;&nbsp;:white_check_mark: Url to a site with a template;  
&nbsp;&nbsp;&nbsp;&nbsp;:white_check_mark: All images for each template;  
&nbsp;&nbsp;&nbsp;&nbsp;:white_check_mark: Template description.  

## How to run the parser? :rocket:

:bangbang: You must have installed Python and Git :bangbang:

1. First you need to clone this repozitory:
   - Create some folder;
   - Copy the path to this folder:  
   ![Copy Path Guide Image](https://i.imgur.com/aG9oR0J.png)  
   - Open CMD;
   - Go to this folder. To do this enter the command:
     ```
     cd <path>
     ```  
     ![Cd cmd guide image](https://i.imgur.com/PPBy1WP.png)
   - Next you need to clone the repository using the command:
     ```
     git clone https://github.com/danisimore/LandingfolioParser.git
     ```
     ![Cd cmd guide image](https://i.imgur.com/vn5nfYq.png)    
   - If you did everything correctrly you will have the `LandigfolioParser` folder;
   - Next you need to go to this folder using command:
     ```
     cd LandigfolioParser
     ```  
     And install requirements. To do this enter the command:
     ```
     pip install -r requirements.txt
     ```
     :pushpin: ***You can also create a virtual envirenment before you install requirements. To do this enter the command  
      `python -m venv venv`. When venv is created, you need to activate it. Enter into the console: `.\venv\Scripts\activate`. Thereafter install the requirements.***
   - Next you need to go to the `landingfolio_parser` using command:  
      ```
     cd landingfolio_parser
      ```
   - It remains only to run the script. To do this enter the command:
     ```
     python main.py
     ```
     **Done!** :tada::tada::tada:

## What happens when the parser does the job? :sparkles:
1. The `result_list.json` file will be created in the `landingfolio_parser` directory. This file will contain a list with dictionary, like:
  ```
  [
      {
          "title": "Rewind",
          "url": "https://www.rewind.ai/",
          "images": [
              "https://landingfoliocom.imgix.net/inspiration/1695253955478Rewinddesktop7bbb5e550a45430d9985163273ec1936png",
              "https://landingfoliocom.imgix.net/inspiration/1695253955501Rewinddesktop9989ef17d14e45eea15836822f5b0da8png",
              "https://landingfoliocom.imgix.net/inspiration/1695253955507Rewinddesktopa05b5c7e556a42b09ae66bd850359e48png",
              "https://landingfoliocom.imgix.net/inspiration/1695253955512Rewinddesktop2630d0f0a30c46e8acf58f0ba04752e4png"
          ],
          "description": "Rewind is a personalized AI powered by everything you’ve seen, said, or heard."
      },
  ```
2. An images will be downloaded to the data directory. The images will be saved in the folders whose name corresponds to the templates title. **For example**:
  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![Data folder example](https://i.imgur.com/Q0TMbNf.png)

## How it works? :hammer_and_wrench:
1. We run the `main.py` file :runner:;
2. The `main()` function is called when the `main.py` is started;
3. The `main()` function calls the `get_data_file()` function and passes it an argument with the request headers;
4. During execution `get_data_file()` function calls `get_description()` function.  `get_description()` function collect a description from each template detail page and returns this description.
5. After the completion, the function `get_data_file()` create the `result_list.json` file an example of which is given above;
6. Next, the `main()` function calls `download_images()` function and passes it an argument with the path to the json file;
7. After the completion, the function `download_images()` saves all images of each landing template along the path `data/<template_name>/<download_sequence_number>.png`.

    
