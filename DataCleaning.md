# Data Cleaning

The dataset that we were used for this project provided by Heartland Family Service (HFS). The goal was to find some relevant questions and analyze the data that can be helpful for the future decision making of the company. The dataset contains data about the services attended by the clients and few details of the clients of HFS as well. There are a total of 8745 rows of data for 51 columns.

Read the data
```R
HFS <- read.csv("../../HFS Service Data.csv")
```

# Variables that were focused for data cleaning
Based on the research questions, we are mainly focusing on the following variables: program name, facility, job title, staff name, record id, gender identity, age, simple race, zip, state, general location, and event name.

# Research Questions
Our research questions are
<ol>
  <li>What is the case load with respect to programs, job titles, and staff? </li>
  <li>Based on the program, what demographics are currently being served? </li>
  <li>Using american community survey data, are the percent of demographics of both the population served in the 680 and 681 area codes (non-telehealth and telehealth specified *Row AD General Location*)  and the percent of the demographics in Douglas county with access to internet fairly similar to each other? </li>
  <li>What care comes from which facilities based on job title, Sc code, zip, and state?</li>
</ol>

## Cleaning for Research Question 1
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The specific variables being used are program name, facility, record id, job title, and staff name. The table below demonstrates the information about cleaning in a table form. According to this table, we know that there are not missing values for these variable and that all the data is standardized. Therefore, this data does not need cleaning with regards to missing values and un-standardized values.

<table style="border: 1px solid black; width: 100%;">
    <thead style="border: 1px solid black">
        <tr>
            <th colspan="4" style="background-color: #04AA6D; color: white;">Column name</th>
            <th colspan="4" style="background-color: #04AA6D; color: white;">Missing values</th>
            <th colspan="4"style="background-color:#04AA6D; color: white;">Unstandardised values</th>
        </tr>
    </thead>
    <tbody>
        <tr style="background-color: #f2f2f2; text-align: center;">
            <td colspan="4" > program_name </td>
            <td colspan="4" > x </td>
            <td colspan="4" >x</td>
        </tr>
        <tr style="text-align: center;">
            <td colspan="4" >facility</td>
            <td colspan="4" >x</td>
            <td colspan="4" >x</td>
        </tr>
        <tr style="background-color: #f2f2f2; text-align: center;">
            <td colspan="4" >job_title</td>
            <td colspan="4" >x</td>
            <td colspan="4" >x</td>
        </tr>
        <tr style="text-align: center;">
            <td colspan="4" >staff_name</td>
            <td colspan="4" >x</td>
            <td colspan="4" >x</td>
        </tr>
        <tr style="background-color: #f2f2f2; text-align: center;">
            <td colspan="4" > recordID </td>
            <td colspan="4" >x</td>
            <td colspan="4" >x</td>
        </tr>
    </tbody>
</table>
<br/>

<p> the variables were compared based on the below table:</p>
<table style="border: 1px solid black; width: 100%;">
  <thead style="border: 1px solid black">
    <tr>
      <th colspan="6" style="background-color: #04AA6D; color: white;"> Independent </th>
      <th colspan="6" style="background-color: #04AA6D; color: white;"> Dependent </th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6" >Program name</td>
      <td colspan="6" >Unique Record id </td>
    </tr>
    <tr style="text-align: center;">
      <td colspan="6">Program name</td>
      <td colspan="6">Job Title</td>
    </tr>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6">Program name</td>
      <td colspan="6">Unique Staff Name</td>
    </tr>
    <tr style="text-align: center;">
      <td colspan="6">Program name</td>
      <td colspan="6">Staff Name</td>
    </tr>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6">Facility</td>
      <td colspan="6">Job Title</td>
    </tr>
    <tr style="text-align: center;">
      <td colspan="6">Facility</td>
      <td colspan="6">Unique Staff Name</td>
    </tr>
  </tbody>
</table>


### Table 1 and Table 1 Metadata
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; We subset the data based on the research questions. The first table was included Program name and Unique Record ID. In this data set, we were able to show the amount of patients in each program. The amount of patients that were in multiple programs can also be showed by the table.

```R
Program_ID11 <- unique(HFS[ , c('recordID', 'program_name')])
as.data.frame(table(Program_ID11$program_name))
```

<p> The amount of patients in each program:</p>
<table style="border: 1px solid black; width: 100%;">
  <thead style="border: 1px solid black">
    <tr>
      <th colspan="6" style="background-color: #04AA6D; color: white;"> Program name </th>
      <th colspan="6" style="background-color: #04AA6D; color: white;"> Frequency </th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6" >Gambling</td>
      <td colspan="6" >8 </td>
    </tr>
    <tr style="text-align: center;">
      <td colspan="6">Mental health</td>
      <td colspan="6">482</td>
    </tr>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6">Substance use</td>
      <td colspan="6">88</td>
    </tr>
  </tbody>
</table>


```R
as.data.frame(table(Program_ID11$program_name))
```

<p> The amount of patients that were admitted on multiple program
(in this table, we showed a demo by only providing first 5 recordID)</p>
<table style="border: 1px solid black; width: 100%;">
  <thead style="border: 1px solid black">
    <tr>
      <th colspan="6" style="background-color: #04AA6D; color: white;"> recordID </th>
      <th colspan="6" style="background-color: #04AA6D; color: white;"> how many programs attend </th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6" >1</td>
      <td colspan="6" >1 </td>
    </tr>
    <tr style="text-align: center;">
      <td colspan="6">2</td>
      <td colspan="6">2</td>
    </tr>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6">3</td>
      <td colspan="6">2</td>
    </tr>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6">4</td>
      <td colspan="6">1</td>
    </tr>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6">5</td>
      <td colspan="6">2</td>
    </tr>
  </tbody>
</table>


### Table 2 and Table 2 Metadata
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The second data table was included by Program name, Facility name, and Job Tile variables. The subset of HFS dataset (table 2) showed which job titles are used more for specific programs and facilities.

```R
Program_Facility_Staff12<-subset(HFS[,c('program_name','facility', 'job_title')])
as.data.frame(table(Program_Facility_Staff12$program_name))
```
<p> The amount of patients in each program based on facility and job title:</p>
<table style="border: 1px solid black; width: 100%;">
  <thead style="border: 1px solid black">
    <tr>
      <th colspan="6" style="background-color: #04AA6D; color: white;"> Program name </th>
      <th colspan="6" style="background-color: #04AA6D; color: white;"> Frequency </th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6" >Gambling</td>
      <td colspan="6" >87 </td>
    </tr>
    <tr style="text-align: center;">
      <td colspan="6">Mental health</td>
      <td colspan="6">6860</td>
    </tr>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6">Substance use</td>
      <td colspan="6">1798</td>
    </tr>
  </tbody>
</table>

```R
as.data.frame(table(Program_Facility_Staff12$facility))
```
<p> The facility that were used more frequently based on specific programs and facilities.
(in this table, we showed a demo by only providing first 5 job titles)</p>
<table style="border: 1px solid black; width: 100%;">
  <thead style="border: 1px solid black">
    <tr>
      <th colspan="6" style="background-color: #04AA6D; color: white;"> Facility </th>
      <th colspan="6" style="background-color: #04AA6D; color: white;"> how many programs attend </th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6" >Abraham Lincoln High School</td>
      <td colspan="6" >17 </td>
    </tr>
    <tr style="text-align: center;">
      <td colspan="6">Bellevue Reporting Center</td>
      <td colspan="6">130</td>
    </tr>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6">Center Mall Office</td>
      <td colspan="6">414</td>
    </tr>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6">Heartland Family Service - Central</td>
      <td colspan="6">1359</td>
    </tr>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6">Heartland Family Service - Child and Family Center</td>
      <td colspan="6">653</td>
    </tr>
  </tbody>
</table>

```R
as.data.frame(table(Program_Facility_Staff12$job_title))
```
<p> The job titles that were used more frequently based on specific programs and facilities.
(in this table, we showed a demo by only providing first 5 job titles)</p>
<table style="border: 1px solid black; width: 100%;">
  <thead style="border: 1px solid black">
    <tr>
      <th colspan="6" style="background-color: #04AA6D; color: white;"> Job titles </th>
      <th colspan="6" style="background-color: #04AA6D; color: white;"> how many programs attend </th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6" >ADMIN ASST</td>
      <td colspan="6" >292 </td>
    </tr>
    <tr style="text-align: center;">
      <td colspan="6">Billing Specialist</td>
      <td colspan="6">5</td>
    </tr>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6">Case Coordinator</td>
      <td colspan="6">12</td>
    </tr>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6">CASE MANAGERS</td>
      <td colspan="6">371</td>
    </tr>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6">Clinical Director</td>
      <td colspan="6">31</td>
    </tr>
  </tbody>
</table>

### Table 3 and Table 3 Metadata

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The final table that we used for this research question was included by Program name, Facility name, and Unique Staff Title. We used this table in order to see whether staff are splitting their time between more than one facility or not.

```R
Program_Facility_uStaff13 <- unique(HFS[ , c('facility', 'program_name','staff_name' )])
as.data.frame(table(Program_Facility_uStaff13$program_name))
```
<p> The amount of patients in each program based on facility and staff_name:</p>
<table style="border: 1px solid black; width: 100%;">
  <thead style="border: 1px solid black">
    <tr>
      <th colspan="6" style="background-color: #04AA6D; color: white;"> Program name </th>
      <th colspan="6" style="background-color: #04AA6D; color: white;"> Frequency </th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6" >Gambling</td>
      <td colspan="6" >10 </td>
    </tr>
    <tr style="text-align: center;">
      <td colspan="6">Mental health</td>
      <td colspan="6">165</td>
    </tr>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6">Substance use</td>
      <td colspan="6">64</td>
    </tr>
  </tbody>
</table>

```R
as.data.frame(table(Program_Facility_uStaff13$facility))
```
<p> The facility that were used more frequently based on program_name and staff_name.
(in this table, we showed a demo by only providing first 5 job titles)</p>
<table style="border: 1px solid black; width: 100%;">
  <thead style="border: 1px solid black">
    <tr>
      <th colspan="6" style="background-color: #04AA6D; color: white;"> Facility </th>
      <th colspan="6" style="background-color: #04AA6D; color: white;"> how many programs and facility attend </th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6" >Abraham Lincoln High School</td>
      <td colspan="6" >3</td>
    </tr>
    <tr style="text-align: center;">
      <td colspan="6">Bellevue Reporting Center</td>
      <td colspan="6">8</td>
    </tr>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6">Center Mall Office</td>
      <td colspan="6">8</td>
    </tr>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6">Heartland Family Service - Central</td>
      <td colspan="6">38</td>
    </tr>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6">Heartland Family Service - Child and Family Center</td>
      <td colspan="6">16</td>
    </tr>
  </tbody>
</table>

```R
as.data.frame(table(Program_Facility_Staff12$staff_name))
```
<p> The staff name that were used more frequently based on program_name and facilities.
(in this table, we showed a demo by only providing first 5 job titles)</p>
<table style="border: 1px solid black; width: 100%;">
  <thead style="border: 1px solid black">
    <tr>
      <th colspan="6" style="background-color: #04AA6D; color: white;"> Staff name </th>
      <th colspan="6" style="background-color: #04AA6D; color: white;"> how many programs and facility attend </th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6" >Anderson, Florentina</td>
      <td colspan="6" >292 </td>
    </tr>
    <tr style="text-align: center;">
      <td colspan="6">Anderson, Melanie</td>
      <td colspan="6">3</td>
    </tr>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6">Barker, Emily</td>
      <td colspan="6">1</td>
    </tr>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6">Barrett, Becky</td>
      <td colspan="6">1</td>
    </tr>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6">Bundy, Nicholas</td>
      <td colspan="6">1</td>
    </tr>
  </tbody>
</table>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Please note that before, during, and after the data was subset-ed, we considered what data we were not using. We found the impact was negligible with respect to the research question (What is the case load with respect to programs, job titles, and staff?).

## Cleaning for Research Question 2

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The specific variables being used were program name, age filtered by the unique record id, gender identity filtered by the unique record id, and race filtered by the unique record id. The following table showed the demonstration of the information about cleaning of the variables.

<table style="border: 1px solid black; width: 100%;">
    <thead style="border: 1px solid black">
        <tr>
            <th colspan="4" style="background-color: #04AA6D; color: white;">Column name</th>
            <th colspan="4" style="background-color: #04AA6D; color: white;">Missing values</th>
            <th colspan="4"style="background-color:#04AA6D; color: white;">Unstandardised values</th>
        </tr>
    </thead>
    <tbody>
        <tr style="background-color: #f2f2f2; text-align: center;">
            <td colspan="4" > program_name </td>
            <td colspan="4" >x</td>
            <td colspan="4" >x</td>
        </tr>
        <tr style="text-align: center;">
            <td colspan="4" >gender_identity</td>
            <td colspan="4" >x</td>
            <td colspan="4" >✓</td>
        </tr>
        <tr style="background-color: #f2f2f2; text-align: center;">
            <td colspan="4" >age</td>
            <td colspan="4" >x</td>
            <td colspan="4" >x</td>
        </tr>
        <tr style="text-align: center;">
            <td colspan="4" >simple_race</td>
            <td colspan="4" >x</td>
            <td colspan="4" >✓</td>
        </tr>
        <tr style="background-color: #f2f2f2; text-align: center;">
            <td colspan="4" > recordID </td>
            <td colspan="4" >x</td>
            <td colspan="4" >x</td>
        </tr>
    </tbody>
</table>

<br/>
