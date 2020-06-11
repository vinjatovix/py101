const fs = require('fs');


var strArray = []
var chunksArray = []
var smallestNum = 0;
var decryptedStr = '';

function convertToStringArray() {
    rawStr = fs.readFileSync('data.txt', 'utf8')
    rawStr.split(' ').join();
    rawStr = rawStr.replace(/\s/g, '')
    strArray = rawStr.split('.');
    strArray.shift() //remove first element which is blank
}


function totalEveryThreeElements() {
    var tripletCount = 1;
    var sumTriplet = 0;
    for (var i = 0; i < strArray.length; i++) {
        if (tripletCount <= 3) {
            sumTriplet += parseInt(strArray[i]);
            tripletCount++;
        }
        if (tripletCount > 3) {
            chunksArray.push(sumTriplet);
            tripletCount = 1;
            sumTriplet = 0;
        }
    }
    fs.writeFileSync('data2.txt', chunksArray);
}

function getSmallestNumber() {
    smallestNum = Math.min(...chunksArray);
    console.log(smallestNum);
}

function convertToAscii(offset) {
    for (var i = 0; i < chunksArray.length; i++) {
        minusPassword = parseInt(chunksArray[i]) - offset;
        character = String.fromCharCode(minusPassword);
        decryptedStr += character;
    }
    console.log('\r\n');
    console.log(decryptedStr);

}

function getNumberOfNonPrintableChars(offset) {
    var numOfNonPrintableChars = 0;
    for (var i = 0; i < chunksArray.length; i++) {
        minusPassword = parseInt(chunksArray[i]) - offset;
        if (minusPassword < 32 || minusPassword > 126) {
            numOfNonPrintableChars++;
        }
    }
    return numOfNonPrintableChars;
}

function bruteForce() {
    for (var i = 0; i <= smallestNum; i++) {
        numOfNonPrintableChars = getNumberOfNonPrintableChars(i);
        if (numOfNonPrintableChars < 15) {
            console.log('--------found: ' + i + '-----------');
            convertToAscii(i);
        }
    }
}

function start() {
    convertToStringArray();
    totalEveryThreeElements();
    getSmallestNumber();
    bruteForce();
}


start();