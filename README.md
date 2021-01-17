# Hack-The-North-2020++
Smart Lecture

## Inspiration: 
- This idea stems from my online semester at school when I was reviewing for final exams. Every single lecture is over an hour long and I was trying to rush though them at 4x video speed, wishing if only I could have a tool that helped me watching the only lecture parts I really needed. This project is a step closer to that idea.

Project: 
- Application takes in a lecture video and uses a machine learning Algorithmia API to split the video intelligently based on keyframes into smaller chunks. For each of these smaller clip, we extract the audio and use MS Azure Speech-to-Text to convert to pure text; then we continue to use Azure Text Analytics API to get keywords from those audio. With some file manipulation/arrangement and few more small algorithms, the project is able to return a list of subvideos correspond most to keywords that users entered. 

- Run smartlecture.py file

** UPDATE: 
- As of now the application is sadly not finished as it's missing the entire front-end for the user to interact with. I'm a first-timer at a hackathon and we're both beginners at building an entire app in general as well as not having much experience at hackathon. We were very busy at using and debugging the APIs as this is the very first time we ever deeply involve in using them. 
- Nevertheless, we tried our best and it's a very open-minded and knowledgable experience that we acquire. We pulled an allnighter brainstorming, learning intensively and struggling with these new tools as we go. 
