'use strict';

const insertion = (arr) => {
  for (let i = 1; i < arr.length; i++) {
    for (let j = 0; j < i; j++) {
      if (arr[i] < arr[j]){
        [arr[i], arr[j]] = [arr[j], arr[i]];
      }
      if (arr[j] % 2 !== 0) {
        [arr[i], arr[j]] = [arr[j], arr[i]]; 
      }
    }
  }
  return arr;
};

const arr = [30, 19, 9, 15, 55, 24, 3, 78, 46, 41];
insertion(arr);

console.log(arr);