<b> Employee Attendance and  Moniteering at Office </b> 

**Installation** (If you do not have node red installed and the nodes already installed) <br> 
**Node-Red**

    1. Open the Terminal window and do: 
        `sudo apt update && sudo apt full-upgrade`

    2. Install Node-red 
    `bash <(curl -sL https://raw.githubusercontent.com/node-red/linux-installers/master/deb/update-nodejs-and-nodered) --node16 ` 

    3. open node-red 
      `cd ~/.node-red` 
      `npm rebuild`
      `node-red-start`

    4. Go to  `http://127.0.0.1:1880`

  5. Install the necessary nodes. Open the Node-RED editor and navigate to the "Manage Palette" menu. Search for and install the following nodes:
    `node-red-dashboard`
    `unisannio-node-red-contrib-grovepi`
    `node-red-contrib-camerapi`
    `node-red-contrib-sqlite`
    `node-red-contrib-azure-iot-device`
    `node-red-node-twilio`
 
 **Azure Computer Vision**  (If you are training your own images) </br>

    1. Create an Azure Custom Vision project: In the Azure portal, navigate to the Custom Vision service, and create a new project. Give your project a name and description, and choose "Classification" as the project type.

    2. Add multiple atleast 50 images of each employee to the project: Upload images to the project, and give them their respective tag `Note : use the name of the employee as the tagNmae`. 

    3. Train the model: After adding images to the project, click on the "Train" button to start training the model. Azure Custom Vision will use your labeled images to train a machine learning model that can classify new images.

    4. Test the model: Once the model has finished training, you can test it by uploading new images to the project and seeing how well it performs. 

    5. Once you are getting expected result,publish the iteraion. 

    6.Click on Prediction key  store your prediction key and the url for the image file path.

**Azure IOT Central Dashboard** ( If you are creating your own Dashboard) </br> 

    1. First you need to create an IOT Central Dashboard. 
    
    2. Then create a new device. 
    
    3. Store the DeviceID, scopeID,Primary Connection String. 
    
    4. After connecting the device to IoT Central, you need to send telemetry readings from the device to the IoT Central hub.You can do that by clicking on manage template --> edit template 
     ---> add Capabilities --> save ---> publish 

**Note: Make sure you keep the Display Name of the capabilities same as the telemetry's you are sending from the node-red**

Finally, to view the device's telemetry readings in the IoT Central dashboard, navigate to the device's details page and click on the "Dashboards" tab.
Here, you should be able to see real-time data from the device, as well as historical data by creating charts. 

**Usage**  (How to run This project on your system ) </br>

      1. Download the flow.json file on your machine. 

      2. Import the Node-RED flow file flow.json into your Node-RED editor.Open Node-red 

      Connect all the sensors to the pin selected in the sensor nodes, 
      Connect all Digital Outputs to the pin selected  in the OutPut nodes. 

      3. Create an Employee table with the Employee's Name and contact number by injecting the create table node.

      4. Insert the values for each column by injecting the insertEmployee  Node [modify the values by changing in the  msg.payload] 

      5. Create Attendance Table by Injecting the create Attendance Node.

      6. Show your face to the camera (It wont work for you, unless you are trained for in the computer vision) Look at the custom vision part to train your own images. 

      The ultrasonic sensor will automatically turn on the camera on detecting faces and send it to the Azure Computer Vision node for face detection and recognition.
      If a face is detected, The employee is marked present for the day. 

      5. You can viewe the charts and anlaytics of presntees/abseentees ,  employee inside office/outside office , name of last entered Employee and name of last exited Employee and
      the `arrival pattern` having low values when person is detected on `localhost:1880/ui`. 
      
      6. To see the Dashboard you can create your oen IOT Central Dashboard using instructions from the Azure IOT central Dashboard section.

**Technologies used:** </br> 
1. Node-red 
2. Azure Custom Vision 
3. Azure IOT Hub and  Iot central Dashboard 
4. SQLite



