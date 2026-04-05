/**
 * Instructions:
 * 1. Open your Spreadsheet.
 * 2. Extensions > Apps Script.
 * 3. Paste this code.
 * 4. Click 'Deploy' > 'New Deployment'.
 * 5. Web App | Execute as: Me | Who has access: Anyone.
 * 6. AFTER SAVING: You MUST click 'Deploy' again if you changed the code!
 */

function doPost(e) {
  try {
    // 1. Open the sheet (use ID if active sheet fails)
    var ss = SpreadsheetApp.getActiveSpreadsheet();
    var sheet = ss.getSheets()[0]; // Get the first sheet
    
    // 2. Parse data from either parameters or the body
    var data = e.parameter;
    if (e.postData && e.postData.contents) {
       var payload = JSON.parse(e.postData.contents);
       data = payload;
    }
    
    // 3. Append the data
    sheet.appendRow([
      new Date(), 
      data.name || "N/A", 
      data.email || "N/A", 
      data.subject || "N/A", 
      data.message || "N/A"
    ]);
    
    return ContentService.createTextOutput(JSON.stringify({"result": "success"}))
      .setMimeType(ContentService.MimeType.JSON);
      
  } catch (err) {
    return ContentService.createTextOutput(JSON.stringify({"result": "error", "error": err.toString()}))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

function doGet(e) {
  return ContentService.createTextOutput("✅ Script is Active and Ready!");
}
