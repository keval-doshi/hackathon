# GRANDMA.md

Grandma, let me explain what I built in the simplest way possible.

---

You know how in every office, there is a computer department called IT. When something goes wrong with the computer, like the email stops working, or someone cannot log in, or the internet is not connecting, people have to stop their work and call that IT person. Sometimes that person is busy, sometimes they take 30 minutes to come, and sometimes it is a very simple problem that anyone could fix if they just knew the steps.

I thought, why not make something that can answer these questions immediately, without waiting for anyone?

So I built a chatbot. A chatbot is like a messaging app, but instead of a real person replying, a computer replies. You type your problem and it tells you exactly what to do, step by step.

---

Now here is the interesting part, Grandma. I did not just connect it to an AI and say "answer everything". That would be too simple and also not very reliable. Instead I did something smarter.

I first created a book of knowledge. I collected all the common IT problems that happen in offices, like cannot sign in to Microsoft, Outlook not working, files not syncing, Teams not loading, and I wrote the proper solutions for each one. This is like a manual that I gave to my chatbot.

When you ask a question, the chatbot first searches this book. If it finds a close enough match, it gives you the answer directly from the book. This is fast, accurate, and does not need the internet or any AI.

But what if you ask something that is not in the book? Maybe a new problem that I did not think of. In that case, the chatbot then goes and asks an AI called Groq, which is like a very knowledgeable person sitting on the internet. That AI thinks about your problem and gives a proper answer.

So basically there are two layers. First the book, then the AI. This is actually how big companies build their support systems.

---

The website also shows you where the answer is coming from. If it came from my book, it shows a green badge that says "Knowledge Base". If it came from the AI, it shows a purple badge that says "AI". This is important because it shows honesty, you know exactly whether a human wrote that answer or a machine figured it out.

It also shows a confidence score, like 87 percent match. This means the chatbot is telling you how sure it is about the answer, which again is something real professional systems do.

---

To build all this, I used Python which is a programming language, Flask which puts the website on the internet, something called FAISS which is the search engine that looks through my book of knowledge, and Groq AI for the smart fallback answers.

I also made it look nice with a dark theme, smooth animations, and you can even give feedback on each answer by clicking thumbs up or thumbs down.

---

The goal was simple, Grandma. If someone in an office is stuck with a computer problem, they should not have to wait. They should just open this, type their problem, and get help in seconds.

I think that is genuinely useful. And I built it myself from scratch.

Made by Keval, your grandson who you always thought was just staring at the screen doing nothing, but was actually building things 😄