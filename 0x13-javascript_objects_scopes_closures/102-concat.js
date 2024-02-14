#!/usr/bin/node

/**
 * Concats 2 files.
 *
 */

const fs = require('fs');
fs.writeFileSync(process.argv[4], fs.readFileSync(process.argv[2], 'utf8') + fs.readFileSync(process.argv[3], 'utf8'));
