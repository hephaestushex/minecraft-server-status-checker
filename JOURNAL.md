# Jul 25: Started the project
## 1h
Quick note, this journal is written after the fact due to Stardance Hardware tracking not being functional yet

My inspo for this is my minecraft server with friends, I wanted to know who's on without opening up my server panel or booting up Modrinth Launcher. I noticed Modrinth gave a readout of people online, so I figured it wouldn't be too hard.

I started off by drafting up a schematic on kicad for the overall hardware. What's nice is the pico has an internal power regulator, so I can feed it 3 AA batteries and I can use it for a while. I chose a 16x2 display for reading the MOTD of the server, and 5 LEDs to determine if 5 separate people are online. There's also a power switch to save battery life.

<img width="1234" height="676" alt="image" src="https://github.com/user-attachments/assets/b89852c5-f02b-496a-8d15-655d9e8c302a" />

From there I started coding the server info retrieval code. I saw a python lib that could be used, mcstatus, but unfortunately it depends on heavy libraries that would not run on my pico w (mainly asyncio). From there I turned to Gemini 3.5 Thinking to create some code to retrieve the server info. The code for this is pretty complex, and I highly doubt I would have figured it out from here. From what I could see, it required composing bytes and creating a socket to send and receive data. Fortunately the code from here is pretty simple.

I stopped from there, and tested my own server for its data. (it's whitelisted so don't bother joining)
<img width="326" height="166" alt="Screenshot 2026-06-25 180344" src="https://github.com/user-attachments/assets/77a25148-530e-4e1a-a820-912b4d220205" />


