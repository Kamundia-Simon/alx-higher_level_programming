#!/usr/bin/node

const [,, myArgs] = process.argv;
if (myArgs === undefined) {
  console.log('No arguments');
} else {
  console.log(myArgs);
}
