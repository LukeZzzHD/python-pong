const { exec } = require("child_process");
const path = require("path");

const pythonFileName = "./main.py";

// Define the path to your Python script
//const pythonScriptPath = path.join(__dirname, pythonFileName);

// Execute the Python script
exec(`python ${pythonFileName}`, (error, stdout, stderr) => {
  if (error) {
    console.error(`Error executing Python script: ${error.message}`);
    return;
  }
  if (stderr) {
    console.error(`Python script stderr: ${stderr}`);
    return;
  }
  console.log(`Python script output: ${stdout}`);
});
