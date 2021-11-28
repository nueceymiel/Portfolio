//Jaime Villa
//1408893
//106 Final Project
//Lorenz Equations

var x, y, z;

var sigma = 10;
var rho = 28;
var beta = 8 / 3;
var s = 80;



function preload() {
}

function setup() {
  createCanvas(windowWidth, windowHeight);
  background(0);
  x = random(3);
  y = random(3);
  z = random(3);
}

var t = 5;
var dt = 0.01;

function Center_x(v) {//arbitrary constant here just to center things
  return windowWidth * (0.5 + x / s);
}
function Center_z(v) {
  return windowHeight * (10 + z)/ s;
}
function Center_y(v) {
  return windowHeight * (0.8 + y / s);
}

function draw() {
  var dx = sigma * (y - x);
  var dy = x * (rho - z) - y;
  var dz = x * y - beta * z;

  x += dx * dt;
  y += dy * dt;
  z += dz * dt;

  stroke('rgb(0,200,255)');
  strokeWeight(10);
  point(Center_y(y), Center_z(z));
}
