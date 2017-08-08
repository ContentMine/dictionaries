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

process.chdir('./json')
fsRDP('./')
.then(readJsonFiles)
.then(function (files) {
  files.map(function (file) {
    var dict = JSON.parse(file)
    if (dict.id) {
      // console.log(dict.id)
    } else {
      var possibleTitles = dict.entries.map(function (entry) {
        return entry.identifiers.contentmine.match(/^([a-zA-Z.]*)/)[1]
      })
      var uniqTitles = _.uniq(possibleTitles)
      if (uniqTitles.length === 1) {
        dict.id = uniqTitles[0]
        fs.writeFile(uniqTitles[0].slice(3) + '.json', JSON.stringify(dict, null, 4))
      }
    }
  })
})
.catch(console.log)
