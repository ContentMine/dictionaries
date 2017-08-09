var fs = require('fs')
var util = require('util')
var _ = require('lodash')

var fsRDP = util.promisify(fs.readdir)
var fsRFP = util.promisify(fs.readFile)

function readJsonFiles (filenames) {
  var foo = filenames.map((file) => {
    return fsRFP(file, { encoding: 'utf8' })
  })
  return (Promise.all(foo))
}

var total = 0

process.chdir('./json')
fsRDP('./')
.then(readJsonFiles)
.then(function (files) {
  files.map(function (file) {
    var dict = JSON.parse(file)
    console.log(dict.id + ' ' + dict.entries.length)
    total = total + dict.entries.length
  })
  console.log('Total: ' + total)
})
