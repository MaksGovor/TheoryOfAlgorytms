'use strict';

const insertion = arr => {
  const map = [
    arr.filter(x => x % 2 === 0),
    arr.filter(x => x % 2 !== 0)
  ];
  for (const res of map){
    for (let i = 0; i < res.length; i++) {
      const val = res[i];
      let j = i - 1;
      while (j >= 0 && res[j] > val) {
        res[j + 1] = res[j];
        j--;
      }
      res[j + 1] = val;
    }  
  }
  return [...map[0] , ...map[1].reverse()];
} 

const arr = [30, 19, 9, 15, 55, 24, 3, 78, 46, 41];
const res = insertion(arr);
console.log(res);
