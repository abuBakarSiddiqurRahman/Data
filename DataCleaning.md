# Data Cleaning and analyze the data after cleaning

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

# Changing row names and remove some rows
gender_identity had some un-standardized values. For example in gender_identity there were instances of “Woman” and “Female”. Additionally there were instances of “Not Obtained” and “NA”. These was standardized by changing row names for gender identity column. “Not Collected” and “Unknown” character was replaced by NA (in total 50 rows name changed by NA in gender identity column). Now the data set contained only NA instead of “Not Collected” and “Unknown”. All "woman" replaced by "Female" in the gender identity column of the dataset.
The simple_race column had values which did not match with the values provided in the SLA Data Columns document. There were a total of 178 records belonging to 11 unique recordIDs. So data was cleaned of such recordIDs for this research question. The recordIDs that were cleaned where - 19, 111, 135, 191, 219, 226, 227, 394,407, 421, 463.

```R
HFS$gender_identity[HFS$gender_identity=="Woman"] <- "Female"
HFS$gender_identity[HFS$gender_identity=="Not Obtained"] <- "NA"
HFS$gender_identity[HFS$gender_identity=="Unknown"] <- "NA"
HFS$gender_identity[is.na(HFS$gender_identity)]<-"NA"

as.data.frame(table(HFS$gender_identity))
```

<p> The gender_identity and its frequency after cleaning from the above mentioned process.
</p>
<table style="border: 1px solid black; width: 100%;">
  <thead style="border: 1px solid black">
    <tr>
      <th colspan="6" style="background-color: #04AA6D; color: white;"> Gender identity </th>
      <th colspan="6" style="background-color: #04AA6D; color: white;"> frequency </th>
    </tr>
  </thead>
  <tbody>
    <tr style="text-align: center;">
      <td colspan="6">Client Declined to Give</td>
      <td colspan="6">48</td>
    </tr>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6">Female</td>
      <td colspan="6">4011</td>
    </tr>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6">Man</td>
      <td colspan="6">4011</td>
    </tr>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6">NA</td>
      <td colspan="6">2442</td>
    </tr>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6">Non-Binary</td>
      <td colspan="6">36</td>
    </tr>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6">Other</td>
      <td colspan="6">24</td>
    </tr>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6">Two-spirit</td>
      <td colspan="6">43</td>
    </tr>
  </tbody>
</table>

```R
as.data.frame(table(HFS2$simple_race))
```
<p> The sample race and its frequency after cleaning the dataset
</p>
<table style="border: 1px solid black; width: 100%;">
  <thead style="border: 1px solid black">
    <tr>
      <th colspan="6" style="background-color: #04AA6D; color: white;"> Sample race </th>
      <th colspan="6" style="background-color: #04AA6D; color: white;"> frequency </th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6" >Asian</td>
      <td colspan="6" >41 </td>
    </tr>
    <tr style="text-align: center;">
      <td colspan="6">Black</td>
      <td colspan="6">835</td>
    </tr>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6">Caucasian</td>
      <td colspan="6">6921</td>
    </tr>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6">Hawaiian Native</td>
      <td colspan="6">10</td>
    </tr>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6">Native American</td>
      <td colspan="6">143</td>
    </tr>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6">Other</td>
      <td colspan="6">5</td>
    </tr>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6">Two or More</td>
      <td colspan="6">265</td>
    </tr>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6">Unknown</td>
      <td colspan="6">347</td>
    </tr>
  </tbody>
</table>

<p> For reserach questions 2 (RQ 2), the following table was considered for analysis
</p>
<table style="border: 1px solid black; width: 100%;">
  <thead style="border: 1px solid black">
        <tr>
            <th colspan="6" style="background-color: #04AA6D; color: white;">Independent (for RQ 2)</th>
            <th colspan="6" style="background-color: #04AA6D; color: white;">Dependent (for RQ 2)</th>
        </tr>
    </thead>
    <tbody>
        <tr style="background-color: #f2f2f2; text-align: center;">
            <td colspan="6" > program_name </td>
            <td colspan="6" >Gender Identity filtered by the Unique Record id (table 4)</td>
        </tr>
        <tr style="text-align: center;">
            <td colspan="6" >program_name</td>
            <td colspan="6" >Age filtered by the Unique Record id (table 5)</td>
        </tr>
        <tr style="background-color: #f2f2f2; text-align: center;">
            <td colspan="6" >program_name</td>
            <td colspan="6" >Race filtered by the Unique Record id (table 6)</td>
        </tr>
    </tbody>
</table>

### Table 4 and Table 4 Metadata
```R
# creating table only with recordID, gender_identity and program_name
Program_Gender_uID21 <- unique(HFS[ , c('recordID', 'gender_identity', 'program_name')])

# gender_identity filetered by unique recordID
as.data.frame(table(Program_Gender_uID21$gender_identity))
```
<p> The gender_identity and its frequency after filtering by unique recordID
</p>
<table style="border: 1px solid black; width: 100%;">
  <thead style="border: 1px solid black">
    <tr>
      <th colspan="6" style="background-color: #04AA6D; color: white;"> Gender identity </th>
      <th colspan="6" style="background-color: #04AA6D; color: white;"> frequency </th>
    </tr>
  </thead>
  <tbody>
    <tr style="text-align: center;">
      <td colspan="6">Client Declined to Give</td>
      <td colspan="6">4</td>
    </tr>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6">Female</td>
      <td colspan="6">255</td>
    </tr>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6">Man</td>
      <td colspan="6">165</td>
    </tr>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6">NA</td>
      <td colspan="6">149</td>
    </tr>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6">Non-Binary</td>
      <td colspan="6">2</td>
    </tr>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6">Other</td>
      <td colspan="6">1</td>
    </tr>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6">Two-spirit</td>
      <td colspan="6">2</td>
    </tr>
  </tbody>
</table>

### Table 5 and Table 5 Metadata
```R
# creating table only with recordID, age and program
Program_Gender_uID21 <- unique(HFS[ , c('recordID', 'gender_identity', 'program_name')])

# age distributions for each program that was filtered by unique recordID
as.data.frame(table(Program_Gender_uID21$gender_identity))
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
      <td colspan="6" >2 </td>
    </tr>
    <tr style="text-align: center;">
      <td colspan="6">2</td>
      <td colspan="6">3</td>
    </tr>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6">3</td>
      <td colspan="6">2</td>
    </tr>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6">4</td>
      <td colspan="6">3</td>
    </tr>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6">5</td>
      <td colspan="6">3</td>
    </tr>
  </tbody>
</table>

```R
# observe the age distributions to find out how much of the distributions were related more than a program
as.data.frame(table(Program_Age_uID22$program_name))
```
<p> Age distributions in each program:</p>
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
      <td colspan="6">606</td>
    </tr>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6">Substance use</td>
      <td colspan="6">108</td>
    </tr>
  </tbody>
</table>

### Table 6 and Table 6 Metadata
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The third table included Program name and the Race that was filtered by the Unique Record ID. The race data was cleanead in previous section. Now, the dataset contained 8567 cleaned entries, 567 of them are unique.  The races of the patients involved in programs or a single program showed in this section.

```R
# creating table only with recordID, simple_race and program_name
Program_Race_uID23 <- unique(HFS2[, c('recordID', 'simple_race', 'program_name')])

# sample_race distributions for each program that was filtered by unique recordID
as.data.frame(table(Program_Race_uID23$simple_race))
```
<p> The sample race and its frequency after cleaning the dataset
</p>
<table style="border: 1px solid black; width: 100%;">
  <thead style="border: 1px solid black">
    <tr>
      <th colspan="6" style="background-color: #04AA6D; color: white;"> Sample race </th>
      <th colspan="6" style="background-color: #04AA6D; color: white;"> frequency </th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6" >Asian</td>
      <td colspan="6" >41 </td>
    </tr>
    <tr style="text-align: center;">
      <td colspan="6">Black</td>
      <td colspan="6">835</td>
    </tr>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6">Caucasian</td>
      <td colspan="6">6921</td>
    </tr>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6">Hawaiian Native</td>
      <td colspan="6">10</td>
    </tr>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6">Native American</td>
      <td colspan="6">143</td>
    </tr>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6">Other</td>
      <td colspan="6">5</td>
    </tr>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6">Two or More</td>
      <td colspan="6">265</td>
    </tr>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6">Unknown</td>
      <td colspan="6">347</td>
    </tr>
  </tbody>
</table>

```R
# observe the sample_race distributions to find out how much of the distributions were related more than a program
as.data.frame(table(Program_Race_uID23$program_name))
```
<p> Age distributions in each program:</p>
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
      <td colspan="6">471</td>
    </tr>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6">Substance use</td>
      <td colspan="6">88</td>
    </tr>
  </tbody>
</table>

## Cleaning for Research Question 3

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; This research question was meant to be a secondary question to research question 2. The specific variables being used were general location, age filtered by the unique record id, gender identity filtered by the unique record id, and race filtered by the unique record id. We carried over the cleaning that was done in Question 2's cleaning. General location was cleaned by removing blanks and "Use when no other code fits" values. Then "Telehealth by video" and "Telehealth by call" were grouped together as just "Telehealth".


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
            <td colspan="4" > general_location </td>
            <td colspan="4" >✓</td>
            <td colspan="4" >✓</td>
        </tr>
    </tbody>
</table>

```R
# cleaning for general_location
HFS$general_location[HFS$general_location=="Telehealth - Phone" | HFS$general_location=="Telehealth - Video"] <- "Telehealth"
HFS$general_location[HFS$general_location!="Telehealth"] <- "Not Telehealth"
as.data.frame(table(HFS$general_location))
```

<p> Cleaning general_location based on telehealth and not telehealth classification</p>
<table style="border: 1px solid black; width: 100%;">
  <thead style="border: 1px solid black">
    <tr>
      <th colspan="6" style="background-color: #04AA6D; color: white;"> general_location </th>
      <th colspan="6" style="background-color: #04AA6D; color: white;"> Frequency </th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6" >not telehealth</td>
      <td colspan="6" >4136 </td>
    </tr>
    <tr style="text-align: center;">
      <td colspan="6">telehealth</td>
      <td colspan="6">4609</td>
    </tr>
  </tbody>
</table>

### Background Information on ACS Data
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The ACS County data showed the access to internet by county. The populations were broken down by race, age, education, and employed/unemployed. We used this data set because it showed the population that had access to internet. Thus this was the population that had the capability to use telehealth services. The ACS county data mainly used social determinants in order to compare to access of internet. Therefore, we must clean both data sets in order to compare them. It did not have any gender or gender identity column, so gender section did not compared. However it had race and age. The only races the ACS Data had are: white, black, and asian. It also had the ages split into two categories: 18-64 and 65+. Therefore, we modified our data to be similar. We filtered the HFS simple_race column to only show white, black, and asian.

```R
#ACS Dataset
ACS <- read_excel("../../ACS Cleaned.xlsx")
head(ACS)
```
<table style="border: 1px solid black; width: 100%;">
  <thead style="border: 1px solid black">
    <tr>
      <th colspan="6" style="background-color: #04AA6D; color: white;"> white </th>
      <th colspan="6" style="background-color: #04AA6D; color: white;"> black </th>
      <th colspan="6" style="background-color: #04AA6D; color: white;"> asian </th>
      <th colspan="6" style="background-color: #04AA6D; color: white;"> age 18-64 </th>
      <th colspan="6" style="background-color: #04AA6D; color: white;"> age 65+ </th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6" >0.8620501	 </td>
      <td colspan="6" >0.5710947	 </td>
      <td colspan="6" >0.8936725 </td>
      <td colspan="6" > 0.8205564	</td>
      <td colspan="6" > 0.6245212 </td>
    </tr>
  </tbody>
</table>

```R
# The code was used to rename the rows name on for age groups for telehealth dataset
Telehealth<- unique(HFS[,c('recordID', 'age','simple_race', 'general_location')])
Telehealth$age[Telehealth$age %in% c("18", "19", "20", "21","22",
                     "23", "24", "25", "26", "27",
                     "28", "29", "30", "31", "32", "33",
                     "34", "35", "36", "37", "38",
                     "39", "40", "41", "42", "43", "44",
                     "45", "46", "47", "48", "49", "50",
                     "51", "52", "53", "54",
                     "55", "56", "57", "58", "59", "60",
                     "61", "62", "63", "64")] <- "18 to 64"
Telehealth$age[Telehealth$age %in% c("65", "66", "67", "68","69",
                     "70", "71", "72")] <- "65 or older"
Telehealth$age[Telehealth$age!="18 to 64" & Telehealth$age!= "65 or older"] <- "Remove"
Telehealth<-subset(Telehealth, age!="Remove")
Telehealth$simple_race[Telehealth$simple_race==1] <- "Caucasian"
Telehealth$simple_race[Telehealth$simple_race==8] <- "Asian"
Telehealth$simple_race[Telehealth$simple_race==16] <- "Black"
Telehealth<-subset(Telehealth, simple_race=="Caucasian" | simple_race=="Asian" | simple_race=="Black")
Telehealth1 <- Telehealth[Telehealth$general_location %in% c("Telehealth"), ]
Not<- Telehealth[Telehealth$general_location %in% c("Not Telehealth"), ]
TeleRace<-as.data.frame(table(Telehealth1$simple_race))
TeleAge<-as.data.frame(table(Telehealth1$age))
total=nrow(Telehealth1)+nrow(Not)
AsianTele<-TeleRace[1,2]/total
BlackTele<-TeleRace[2,2]/total
WhiteTele<-TeleRace[3,2]/total
youngerTele<-TeleAge[1,2]/total
olderTele<-TeleAge[2,2]/total
NotTeleRace<-as.data.frame(table(Not$simple_race))
NotTeleAge<-as.data.frame(table(Not$age))
AsianTeleNot<-NotTeleRace[1,2]/total
BlackTeleNot<-NotTeleRace[2,2]/total
WhiteTeleNot<-NotTeleRace[3,2]/total
youngerTeleNot<-NotTeleAge[1,2]/total
olderTeleNot<-NotTeleAge[2,2]/total
```

Code for getting the percentage of each dataset based on race. This data was different because we were looking at the percentage of the demographics using telehealth and those who did not use telehealth.
```R
ACS<-as.tibble(ACS)
Tele<-c(WhiteTele, BlackTele, AsianTele, youngerTele, olderTele)
Not<-c(WhiteTeleNot, BlackTeleNot, AsianTeleNot, youngerTeleNot, olderTeleNot)
ACS<-rbind(ACS,Tele,Not)
Title <- c("ACS", "Telehealth","NotTelehealth")
ACS<-cbind(ACS,Title)

#the percentage of each dataset based on race
ACS<-t(ACS)
colnames(ACS)<-c("ACS", "Telehealth","NotTelehealth")
ACS<-ACS[-c(6), ]
head(ACS)
```
<table style="border: 1px solid black; width: 100%;">
  <thead style="border: 1px solid black">
    <tr>
      <th colspan="6" style="background-color: #04AA6D; color: white;"> Race </th>
      <th colspan="6" style="background-color: #04AA6D; color: white;"> ACS dataset </th>
      <th colspan="6" style="background-color: #04AA6D; color: white;"> Telehealth dataset</th>
      <th colspan="6" style="background-color: #04AA6D; color: white;"> Not telehealth dataset</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6" >	white </td>
      <td colspan="6" >	0.8620501 </td>
      <td colspan="6" >0.4363354 </td>
      <td colspan="6" > 0.4270186	</td>
    </tr>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6" >	black  </td>
      <td colspan="6" >	0.57109470 </td>
      <td colspan="6" > 0.07453416 </td>
      <td colspan="6" > 0.05590062	</td>
    </tr>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6" >	asian </td>
      <td colspan="6" >	0.89367250 </td>
      <td colspan="6" > 0.00310559</td>
      <td colspan="6" > 0.00310559	</td>
    </tr>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6" >	age 18-64 </td>
      <td colspan="6" >	0.8205564 </td>
      <td colspan="6" > 0.5046584</td>
      <td colspan="6" > 0.4829193	</td>
    </tr>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6" >	age 65+ </td>
      <td colspan="6" >	0.62452120 </td>
      <td colspan="6" > 0.00931677</td>
      <td colspan="6" > 0.00310559	</td>
    </tr>
  </tbody>
</table>

<p> we compared the following tables based on the immediate percentage table where we showed the comparison between races for ACS, telehealth and non NotTelehealth dataset

<table style="border: 1px solid black; width: 100%;">
    <thead style="border: 1px solid black">
        <tr>
            <th colspan="4" style="background-color: #04AA6D; color: white;">Percents in HFS Data with Telehealth </th>
            <th colspan="4" style="background-color: #04AA6D; color: white;"> Percents in HFS Data with Non-telehealth </th>
            <th colspan="4" style="background-color: #04AA6D; color: white;"> Percents in ACS County Data with Access to Internet</th>
        </tr>
    </thead>
    <tbody>
        <tr style="background-color: #f2f2f2; text-align: center;">
            <td colspan="4" >Percent of White Population filtered by unique record id and telehealth</td>
            <td colspan="4" >Percent of White Population filtered by unique record id and non-telehealth</td>
            <td colspan="4" >Percent of White Population with access to internet</td>
        </tr>
        <tr style="text-align: center;">
            <td colspan="4" >Percent of Black Population filtered by unique record id and telehealth</td>
            <td colspan="4" >Percent of Black Population filtered by unique record id and non-telehealth</td>
            <td colspan="4" >Percent of Black Population with access to internet</td>
        </tr>
        <tr style="background-color: #f2f2f2; text-align: center;">
            <td colspan="4" >Percent of Asian Population filtered by unique record id and telehealth</td>
            <td colspan="4" >Percent of Asian Population filtered by unique record id and non-telehealth</td>
            <td colspan="4" >Percent of Asian Population with access to internet</td>
        </tr>
        <tr style="text-align: center;">
            <td colspan="4" >Percent of Ages 18 - 64 Population filtered by unique record id and telehealth</td>
            <td colspan="4" >Percent of Ages 18 - 64 Population filtered by unique record id and non-telehealth</td>
            <td colspan="4" >Percent of Ages 18 - 64 Population with access to internet</td>
        </tr>
        <tr style="background-color: #f2f2f2; text-align: center;">
            <td colspan="4" >Percent of Ages 65 or Older Population filtered by unique record id and telehealth</td>
            <td colspan="4" >Percent of Ages 65 or Older Population filtered by unique record id and non-telehealth</td>
            <td colspan="4" >Percent of Ages 65 or Older Population with access to internet</td>
        </tr>
    </tbody>
</table>

## Cleaning for Research Question 4

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The specific variables being used for research question 4 were job title, job title filtered by event name, facility, sc code, zip codes, state, program name, unique record id, staff name, event name.


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
            <td colspan="4" >✓</td>
            <td colspan="4" >x</td>
        </tr>
        <tr style="text-align: center;">
            <td colspan="4" >sc_code</td>
            <td colspan="4" >x</td>
            <td colspan="4" >x</td>
        </tr>
        <tr style="background-color: #f2f2f2; text-align: center;">
            <td colspan="4" > zip </td>
            <td colspan="4" >x</td>
            <td colspan="4" >✓</td>
        </tr>
        <tr style="text-align: center;">
            <td colspan="4" >state</td>
            <td colspan="4" >x</td>
            <td colspan="4" >x</td>
        </tr>
        <tr style="background-color: #f2f2f2; text-align: center;">
            <td colspan="4" > event_name </td>
            <td colspan="4" >x</td>
            <td colspan="4" >x</td>
        </tr>
    </tbody>
</table>

With respect to, sc code we were unsure what the blanks means for the sc code column. In order to not manipulate the data in an unplanned fashion, we decided to make all blanks read “NA”. Finally, there were also some event names that we were categorized differently those contained integer values at the beginning of teir name.

```R
NEIA$event_name[NEIA$event_name=="1. Record Status/Status Update ISMART"] <- "Record Status/Status Update ISMART"
NEIA$event_name[NEIA$event_name=="2. Placement Screening ISMART"] <- "Placement Screening ISMART"
NEIA$event_name[NEIA$event_name=="3. Admission ISMART"] <- "Admission ISMART"
NEIA$event_name[NEIA$event_name=="4. Discharge ISMART"] <- "Discharge ISMART"
NEIA$sc_code[is.na(NEIA$sc_code)]<-"NA"
```

AS column of HFS dataset: Nebraska and Iowa dataset -- Completed by 3614 rows for NE (one data set), 5077 rows for IA (another dataset). Here, two new data sets created.
```R
NEIA <- HFS[HFS$state %in% c("NE","IA"), ]
as.data.frame(table(NEIA$state))
```

<p> Age distributions in each program:</p>
<table style="border: 1px solid black; width: 100%;">
  <thead style="border: 1px solid black">
    <tr>
      <th colspan="6" style="background-color: #04AA6D; color: white;"> State </th>
      <th colspan="6" style="background-color: #04AA6D; color: white;"> Frequency </th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6" >Iowa (IA)</td>
      <td colspan="6" >5077</td>
    </tr>
    <tr style="text-align: center;">
      <td colspan="6">Nebraska (NE)</td>
      <td colspan="6">3614</td>
    </tr>
  </tbody>
</table>


<p> we compared the variables in the following ways for research question 4: </p>
<table style="border: 1px solid black; width: 100%;">
  <thead style="border: 1px solid black">
    <tr>
      <th colspan="6" style="background-color: #04AA6D; color: white;"> Independent </th>
      <th colspan="6" style="background-color: #04AA6D; color: white;"> Dependent </th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6">Job Title</td>
      <td colspan="6">Sc Code</td>
    </tr>
    <tr style="text-align: center;">
      <td colspan="6">Job Title</td>
      <td colspan="6">Zip code</td>
    </tr>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6">Job Title</td>
      <td colspan="6">State</td>
    </tr>
    <tr style="text-align: center;">
      <td colspan="6">Job Title filtered by event name</td>
      <td colspan="6">Sc Code</td>
    </tr>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6">Job Title filtered by event name</td>
      <td colspan="6">Zip code</td>
    </tr>
    <tr style="text-align: center;">
      <td colspan="6">Job Title filtered by event name</td>
      <td colspan="6">State</td>
    </tr>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6">Facility</td>
      <td colspan="6">Program name</td>
    </tr>
    <tr style="text-align: center;">
      <td colspan="6">Facility</td>
      <td colspan="6">Unique Record id</td>
    </tr>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6">Facility</td>
      <td colspan="6">Staff name</td>
    </tr>
    <tr style="text-align: center;">
      <td colspan="6">Facility</td>
      <td colspan="6">Event name</td>
    </tr>
  </tbody>
</table>

### Table 8
```R
# The datset included the variables Job Title, SC code, Zip code, and State including only NE and IA. With this we were able to see the relationship between job title and sc_codes, zip, and state.
Job_SC_Zip_State41 <- subset(NEIA[, c('job_title','sc_code', 'zip', 'state')])
```
### Table 9 and Table 9 Metadata
```R
# The datset included Job Title filtered by event name, SC code, Zip code, and State including only NE and IA. This enabled us to look at job title filtered by event name in relation to sc_code, zip, and state.
filterJob_SC_Zip_State42 <-unique(NEIA[ , c('job_title', 'event_name', 'sc_code','state','zip')])
```

```R
# job_title filtered by event name
head(as.data.frame(table(filterJob_SC_Zip_State42$job_title)))
# event_name filtered by job_title
head(as.data.frame(table(filterJob_SC_Zip_State42$event_name)))
# sc_code filtered by event name
head(as.data.frame(table(filterJob_SC_Zip_State42$sc_code)))
# state filtered by event name
as.data.frame(table(filterJob_SC_Zip_State42$state))
# zip filtered by event name
as.data.frame(table(filterJob_SC_Zip_State42$zip))
```

### Table 10 and Table 10 Metadata

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The third table for this research question included Facility, Program name, Staff Name, Event Name. This enabled us to see the relationship between facility and program_name, staff_name, and event_name.

```R
Facility_Program_Staff_Event43J<- subset(NEIA[, c('facility','program_name', 'staff_name', 'event_name')])
as.data.frame(table(Facility_Program_Staff_Event43J$facility))
as.data.frame(table(Facility_Program_Staff_Event43J$program_name)
head(as.data.frame(table(Facility_Program_Staff_Event43J$staff_name)))
head(as.data.frame(table(Facility_Program_Staff_Event43J$event_name)))
```

### Table 11 and Table 11 Metadata

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Finally the last table helped us to see which facilities were utilized more.

```R
Facility_uID44<-unique(NEIA[ , c('facility', 'recordID')])
as.data.frame(table(Facility_uID44$facility))
```
<p> Facility distributions basd on each recordID (showed here first 5 facilities out of 25 facilities)</p>
<table style="border: 1px solid black; width: 100%;">
  <thead style="border: 1px solid black">
    <tr>
      <th colspan="6" style="background-color: #04AA6D; color: white;"> Facility </th>
      <th colspan="6" style="background-color: #04AA6D; color: white;"> Frequency </th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6" >Abraham Lincoln High School</td>
      <td colspan="6" >3</td>
    </tr>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6" >Bellevue Reporting Center	</td>
      <td colspan="6" >7</td>
    </tr>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6" >Center Mall Office	</td>
      <td colspan="6" >26</td>
    </tr>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6" >Heartland Family Service - Central	</td>
      <td colspan="6" >103</td>
    </tr>
    <tr style="background-color: #f2f2f2; text-align: center;">
      <td colspan="6" >Heartland Family Service - Child and Family Center	</td>
      <td colspan="6" >63</td>
    </tr>
  </tbody>
</table>

## Contributors for the project
##### Abu Bakar Siddiqur Rahman, Lisa Kiemde, Shravya Chandiri
##### Do not hesitate to contact us if you have any questions
##### (abubakarsiddiqurra@unomaha.edu, lgmorton@unomaha.edu, schandiri@unomaha.edu)
