//const dino = $('#dino')
const dino = document.getElementById("dino");
const cuctus = document.getElementById("cactus");
// var score = 0;



function jump() {
    if (dino.classList != "jump") {
        dino.classList.add("jump");
    
        setTimeout(function () {
          dino.classList.remove("jump");
        }, 300);
      }
}


const isAlive = setInterval(myTimer, 10);

function myTimer() {
   // this gets the top of the dino so we can use it for collision detection 
   let dinoTop = parseInt(window.getComputedStyle(dino).getPropertyValue("y"));
   // this gets the x of the cactus so we can use it for collision detection 
   let cactusLeft = parseInt(window.getComputedStyle(cactus).getPropertyValue("x"));
   
//    var scoreTimmer = setInterval(updateScore, 1000);
  // this is collision detection 
  if(cactusLeft < 100 && cactusLeft > 0 && dinoTop >=140) {
    // this case presents a collision 
    // alert("Game Over:(")
    // gameOver = true;
    clearInterval(isAlive);
    // clearInterval(scoreTimmer);
    cactus.classList.remove("cactusAnimate");
    $("#over").css("visibility", "visible");
    listenEnd(true);
    }

    
}

function updateScore() {
    score += 100;
    return $("#score").html(score);
}

// if the game ends, start listening for a button click to restart
function listenEnd (gameFate){
    if(gameFate == true) {
        document.addEventListener("keydown", function (event){
            startGame();
        })
    }
}

function startGame() {
    setInterval(myTimer, 10);
    cactus.classList.add("cactusAnimate");
    $("#over").css("visibility", "hidden");

}







document.addEventListener("keydown", function (event){
    jump();
})