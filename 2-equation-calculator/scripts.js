
// this is a test 
// function testDensity(m) {
//     // var m = $('#density').getElement;
//     // $('#densityResults').val(m);
//     document.getElementById("densityResults").innerHTML = m;
    
// }

// this will calculate density 
function calcDensity() {
    var m = parseInt(document.getElementById("density").value);
    var v = parseInt(document.getElementById("volume").value);
    if (isNaN(m) || isNaN(v)) {
        result = "That's not a number!";
    } else {
        var d = m / v;
        document.getElementById("densityResults").innerHTML = d;
        
    }
        
    
    


}

// this will calculate velocity 
function calcVelocity() {
    var distance = parseInt(document.getElementById("distance").value);
    var time = parseInt(document.getElementById("time").value);

    if (isNaN(distance) || isNaN(time)) {
        result = "That's not a number!";
    } else {
        var v = distance / time;
    }

    
    document.getElementById("velocityResults").innerHTML = v;


}


// this calculates weight 
function calcWeight() {
    var mass = parseInt(document.getElementById("mass").value);
    var gravity = parseInt(document.getElementById("gravity").value);

    if (isNaN(mass) || isNaN(gravity)) {
        result = "That's not a number!";
    } else {
        var weight = mass * gravity;
    }

    

    document.getElementById("weightResults").innerHTML = weight;

}


