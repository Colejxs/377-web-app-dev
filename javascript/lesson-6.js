function printSquares() {
    var items = "";

    var i = 1;
    while (i <= 10) {
        items += "<li>" + Math.pow(i, 2) + "</li>";
        i++;
    }

    document.getElementById("squares").innerHTML = items;
}

function guessName() {
    var guess = prompt("What's my name?");
    var count = 1;

    while (guess != "Bob") {
        guess = prompt("That's not it! Try again.");
        count++;
    }

    alert("You got it! It took you " + count + " guesses.");


}
// This will print the frist 10 powers of 2 
function powersOf2() {
    var powerItems = "";
    var i = 0;
    while (i <= 9) {
        powerItems += "<li>" + Math.pow(2, i) + "</li>";
        i++;
    }
    document.getElementById("powers").innerHTML = powerItems;
}

// this function will make 


