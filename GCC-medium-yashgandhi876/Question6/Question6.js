'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.replace(/\s*$/, '')
        .split('\n')
        .map(str => str.replace(/\s*$/, ''));

    main();
});

function readLine() {
    return inputString[currentLine++];
}

function encrypt(words){
    // Participant's code
    let word = words.split(" ").join("");
    let wordList = word.split("");
    let sq = Math.sqrt(word.length)
    let min = Math.floor(sq);
    let max;
    if((sq - min) === 0){
        max = min
    }else{
        max = min+1;
    }
    let result = ""
    for(let i=0;i<max;i++){
        for(let j=i;j<word.length;j+=max){
            result += wordList[j]
        }
        result += " "
    }
    return result.trim();
}

function main() {
    // const words = readLine();

    const result = encrypt("h");

    // Please do not remove the below line.
    console.log(result)
    // Do not print anything after this line
}