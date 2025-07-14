let grid;
let columns;
let rows;
let resolution = 20
const height = 700
const width = 1000

// this class tracks the state of each cell in the grid
class State {
    constructor(position, cell) {
        cell.state = cell;  // the code reads the cell as either a 0 or 1
    }

    analyze(cell) {
        // take a look at surrounding 8 cells
    }
}

// makes a 2D array to create the grid
function make2DArray(columns, rows) {
    let arr = new Array(columns);
    for (let i = 0; i < arr.length; i++) {
        arr[i] = new Array(rows);
    }
    return arr;
}

// for each element in the 2D array, a number between 0 and 1 is randomly assigned to the element
// this is to create a zeroth generation of the cells
function setup() {
    createCanvas(width, height)
    columns = width / resolution
    rows = height / resolution

    grid = make2DArray(columns, rows);
    for (let i = 0; i < columns; i++) {
        for (let j = 0; j < rows; j++) {
            grid[i][j] = Math.floor(Math.random() * 1.2);
        }
    }   
}

// creates the cells based off the elements' assigned color
function draw() {
    background(0);
    for (let i = 0; i < columns; i++) {
        for (let j = 0; j < rows; j++) {
            let x = i * resolution;
            let y = j * resolution;
            if (grid[i][j] == 1) {
                fill(255);
                rect(x, y, resolution, resolution);
            }
        }
    }
}


