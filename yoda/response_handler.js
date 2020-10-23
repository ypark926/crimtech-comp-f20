// Declaring variables that you may want to use.
let names = ['cute', 'regular'];
let moods = ['dark', 'force', 'std'];

let dark_quotes = ["Once you start down the dark path, forever will it dominate your destiny, consume you it will.",
"In a dark place we find ourselves, and a little more knowledge lights our way.",
"Fear is the path to the dark side. Fear leads to anger. Anger leads to hate. Hate leads to suffering.",
"Always two there are, no more, no less. A master and an apprentice.",
"In the end, cowards are those who follow the dark side."];
let force_quotes = ["Luminous beings are we, not this crude matter.",
"A Jedi uses the Force for knowledge and defense, never for attack.",
"Clear your mind must be, if you are to find the villains behind this plot.",
"The force. Life creates it, makes it grow. Its energy surrounds us and binds us.",
"My ally is the Force, and a powerful ally it is."];
let std_quotes = ["Patience you must have, my young padawan.",
"When nine hundred years old you reach, look as good you will not.",
"No! Try not! Do or do not, there is no try.",
"Judge me by my size, do you?",
"Difficult to see. Always in motion is the future."
];

function respond() {
    var chat = document.getElementById("chat").value;
    console.log(chat);
    var picture_name = "img/";
    var yoda_baby = true;
    var quote = "";

    // CHOOSE PICTURE
    if (chat.includes("cute") || chat.includes("baby")) {
        picture_name += names[0] + "-";
        yoda_baby = true;
    } else {
        picture_name += names[1] + "-";
        yoda_baby = false;
    }

    if (chat.includes("force") && chat.includes("dark")) {
        quote = moods[0];
        picture_name += quote + ".jpg";
    } else if (chat.includes("force")) {
        quote = moods[1];
        picture_name += quote + ".jpg";
    } else {
        quote = moods[2];
        picture_name += quote + ".jpg";
    }

    // CHOOSE RESPONSE
    var yoda_response = "";

    num_of_ms = Math.floor(Math.random()*50+1);
    h = "h";
    ms = "";

    for (let i = 0; i < num_of_ms; i++) {
        ms += "m";
    }

    quote_idx = Math.floor(Math.random()*5);

    if (yoda_baby) {
        yoda_response = "Yes, " + h + ms + ".";
    } else if (quote == moods[0]) {
        yoda_response = dark_quotes[quote_idx];
        console.log("hi")
    } else if (quote == moods[1]) {
        yoda_response = force_quotes[quote_idx];
    } else {
        yoda_response = std_quotes[quote_idx]
    }

    // DISPLAY HTML
    document.getElementById("yodaface").setAttribute("src", picture_name);
    document.getElementById("dialogue").innerHTML = yoda_response;
    document.getElementById("chat").value = "";
}

