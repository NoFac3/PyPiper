{
  "greeting": [
    {
      "tag": "Greeting_General",
      "patterns": [ "hello", "hi", "hey" ],
      "responses": [ "Hello, *n*", "Hi, *n*", "Hey, *n*" ],
      "context_set": ""
    },
    {
      "tag": "Departing_General",
      "patterns": [ "goodbye", "see you later", "see ya" ],
      "responses": [ "Goodbye, *n*", "See you later, *n*", "See ya, *n*" ],
      "context_set": ""
    },
    {
      "tag": "Greeting_Morning",
      "patterns": [ "good morning" ],
      "responses": [ "Good moring, *n*", "Morning, *n*" ],
      "context_set": ""
    },
    {
      "tag": "Greeting_Afternoon",
      "patterns": [ "good afternoon" ],
      "responses": [ "Good afternoon, *n*", "Afternoon, *n*" ],
      "context_set": ""
    },
    {
      "tag": "Greeting_Evening",
      "patterns": [ "good evening" ],
      "responses": [ "Good evening, *n*", "Evening, *n*" ],
      "context_set": ""
    },
    {
      "tag": "Greeting_Night",
      "patterns": [ "good night" ],
      "responses": [ "Good night, *n*" ],
      "context_set": ""
    },
    {
      "tag": "Condition",
      "patterns": [ "*state*, how are you","*state*, how about you","*state*, you" ],
      "responses": [ "I am doing *state*","I am *state*","*state*" ],
      "context_set": ""
    },
    {
      "tag": "Condition_w_reply",
      "patterns": [ "how are you" ],
      "responses": [ "*state*, how are you?", "*state*, how about you?","*state*, you?"],
      "context_set": ""
    }
  ]
}
