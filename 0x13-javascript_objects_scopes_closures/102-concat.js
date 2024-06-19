#!/usr/bin/node
const f = require('f');
const x = f.readFileSync(process.argv[2], 'utf8');
const y = f.readFileSync(process.argv[3], 'utf8');
f.writeFileSync(process.argv[4], x + y);
