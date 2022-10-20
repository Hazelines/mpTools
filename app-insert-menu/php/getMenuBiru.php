<?php 
    // include '../../assets/php/connection.php';

    // $dbname = "MPMIT";

    // $con = mysqli_connect($servername, $username, $password, $dbname);

    // if (!$con) {
    //     die("Connection failed: " . mysqli_connect_error());
    // }
    // echo "Connected successfully";

    // $sql = "SELECT * FROM MPMIT.dbo.MPM_MENU";
    // $result = mysqli_query($con, $sql);

    $res = "<thead>";
    $res .= "<tr>";
    $res .= '<th class="th-sm"> MENU ID </th>';
    $res .= "</tr>";

    $res .= "<tr>";
    $res .= '<th class="th-sm"> CATEGORY ID </th>';
    $res .= "</tr>";

    $res .= "<tr>";
    $res .= '<th class="th-sm"> CATEGORY GROUP ID </th>';
    $res .= "</tr>";

    $res .= "<tr>";
    $res .= '<th class="th-sm"> ORDERED NUMBER </th>';
    $res .= "</tr>";

    $res .= "<tr>";
    $res .= '<th class="th-sm"> PROCESS GROUP NAME </th>';
    $res .= "</tr>";

    $res .= "<tr>";
    $res .= '<th class="th-sm"> MODULE NAME </th>';
    $res .= "</tr>";

    $res .= "<tr>";
    $res .= '<th class="th-sm"> MENU NAME </th>';
    $res .= "</tr>";

    $res .= "<tr>";
    $res .= '<th class="th-sm"> PATH </th>';
    $res .= "</tr>";

    $res .= "</thead>";

    $res .= "<tbody>";

    if (mysqli_num_rows($result) > 0) {
        while($row = mysqli_fetch_assoc($result)) {
            $res .= "<tr>";
            $res .= "<td>".$row['MENU_ID']."</td>";
            $res .= "<td>".$row['CATEGORY_ID']."</td>";
            $res .= "<td>".$row['CATEGORY_GROUP_ID']."</td>";
            $res .= "<td>".$row['ORDERED_NUMBER']."</td>";
            $res .= "<td>".$row['PROCESS_GROUP_NAME']."</td>";
            $res .= "<td>".$row['MODULE_NAME']."</td>";
            $res .= "<td>".$row['MENU_NAME']."</td>";
            $res .= "<td>".$row['PATH']."</td>";
            $res .= "</tr>";
        }
    }

    $res .= "</tbody>";

    // $conn->close();

    echo $res;
?>