var mapCreated = false;
var USMap;
//var initialValuesCalculated = false;
//var selectedState;
var apiKey = 'MY_API_KEY';
var dataYear = '2014';
var povertyCode = 'B17001I_002E'; //Total below poverty level
var totalCode = 'B03001_003E'; //Total Latino population
//var dataYears = ['2010', '2011'];
//var datavariable = 'age';
var dataProcessed = false;
var USData;
var backgroundColor = 195;
//var stateColor;
//var hoverColor = '#a2e0fc';
//var transparency = 100;

function setup() { //things that need to be done only once
  createCanvas(960, 540); 
  initializeCensus('MY_API_KEY'); 
  requestUSData(dataYear, povertyCode);
  requestUSData(dataYear, totalCode);
  requestUSMap();
  //stateColor = color('#18759e');
  //changes colorMode in order to create a gradient
  colorMode(HSB);

  //Loop to go through different data years 
  //for (var i = 0, i < dataYears.length; i++){
  //dataYear(i);      
  //}
}

function draw() {
  background(backgroundColor);
  overMap.clear();    

  //!mapCreated prevents the creation of the map prior to having the data
  if (!mapCreated && USMapIsReady()) {
    USMap = createUSMap(0, 0, width, height);

    //var stateList = USMap.getStateNames();
    //for (var stateIdx in stateList) {
    //  USMap.fill(stateList[stateIdx], 
    //    color(red(stateColor), green(stateColor), blue(stateColor), transparency));
    //  USMap.stroke(stateList[stateIdx], color(backgroundColor));
    //}`
    USMap.show();
    mapCreated = true;
  }

  if (!dataProcessed && USDataIsReady(dataYear, povertyCode) && 
    USDataIsReady(dataYear, totalCode)) {
    var povertyData = getUSData (dataYear, povertyCode);
    var totalData = getUSData (dataYear, totalCode);
    if (mapCreated) {
      var stateNames = USMap.getStateNames();
      for (var i in stateNames) {
        // prints particular data in the console
        print(povertyData[stateNames[i]]);
        print(totalData[stateNames[i]]);
        //A value between 0 and 1. Creates a ratio between total population and population under poverty level
        var ratio = povertyData[stateNames[i]] / totalData[stateNames[i]];
        //establishes minColor and maxColor based on HSB colorMode
        var minColor = color(218, 67, 360); // gradient of colors using HBS/HSL mode
        var maxColor = color(218, 67, 0);
        //lerp is a mapping-like function for color
        USMap.fill(stateNames[i], lerpColor(minColor, maxColor, ratio));
      }
      dataProcessed = true;
    }
  }
}

//function mouseEnter(state) {
//  USMap.fill(state, stateColor);
//}

//function mouseLeave(state) {
//  USMap.fill(state, 
//    color(red(stateColor), green(stateColor), blue(stateColor), transparency));
//}