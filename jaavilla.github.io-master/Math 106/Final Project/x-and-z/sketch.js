//Jaime Villa
//1408893
//106 Final Project
//Lorenz Equations Graph

var x, y, z;

//Lorenz parameters

var sigma = 10;
var rho = 28;
var beta = 8 / 3;
var s = 80;



function preload() {
}
//Creating a canvas
function setup() {
  createCanvas(windowWidth, windowHeight);
  background(0);
  x = random(3);
  y = random(3);
  z = random(3);
}

var t = 4;
var dt = .006;

function Center_x(v) {//arbitrary constant here just to center things
  return windowWidth * (.5 + x / s);
}
function Center_z(v) {
  return windowHeight * (10 + z)/ s;
  
}
function Center_y(v) {
  return windowHeight * (.5 + y / s);
}
//Drawing Lorenz equations
function draw() {
  var dx = sigma * (y - x);
  var dy = x * (rho - z) - y;
  var dz = x * y - beta * z;
  
  

  x += dx * dt;
  y += dy * dt;
  z += dz * dt;

  stroke('rgb(0,200,255)');
  strokeWeight(10);
  point(Center_x(x), Center_z(z));
  
}
