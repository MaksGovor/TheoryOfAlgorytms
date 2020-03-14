'use strict';

class HashSumFinder {
  constructor() {
    this.__iterateLength = 5;
    this.hashTable = new Map();
  }

  generateHash(key) {
    const symbolCode = parseInt(key.toString(2));
    let hash = '';
    let x = 0;
    for (let i = 0; i < this.__iterateLength; i++) {
      hash += String.fromCharCode(symbolCode + x++)
        .charCodeAt(0)
        .toString(28);
    }
    return hash.slice(0, 10);
  }

  addItem(hashLength1, hashLength2) {
    if (!isNaN(parseInt(hashLength1 + hashLength2))) {
      const key = this.generateHash(hashLength1 + hashLength2);
      if (this.hashTable.has(key)) {
        this.hashTable.get(key).push([hashLength1, hashLength2]);
      } else {
        this.hashTable.set(key, [[hashLength1, hashLength2]]);
      }
    }
  }

  findElementsBySum(sum) {
    const key = this.generateHash(sum);
    const k = `Items whose sum is ${sum}`;
    if (this.hashTable.has(key)) return {
       [k]: this.hashTable.get(key),
       colision : this.hashTable.get(key).length 
      };
    return `${k} not found`;
  }
}

//Usage

const array = [1, 4, 5, 6, 3, 2, 10, 11, 14, 18, 12, 17];
const hash1 = new HashSumFinder();
for (let i = 0; i < array.length; i++) {
  for (let j = i; j < array.length; j++)
    hash1.addItem(array[i], array[j]);
}

//console.dir(hash1.hashTable);
const result = [];
const testSum = [9, 18, 14, 65, 432, 7, 11, 133, 20];
testSum.forEach(elem => result.push(hash1.findElementsBySum(elem)));
console.dir(result, {depth: 3});
