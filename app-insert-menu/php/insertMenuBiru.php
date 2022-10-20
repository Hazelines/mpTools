<?php
    $menuId = $_POST['menuId'];
    $categoryId = $_POST['categoryId'];
    $groupId = $_POST['groupId'];
    $groupName = $_POST['groupName'];
    $moduleName = $_POST['moduleName'];
    $menuName = $_POST['menuName'];
    $rolesLine = $_POST['rolesLine'];
    
    $executePython = 'python ../python/insertMenuBiru.py '.$menuId.' '.$categoryId.' '.$groupId.' '.$groupName.' '.$moduleName.' "'.$menuName.'" '.$rolesLine;
    echo $executePython;
    $command = escapeshellcmd($executePython);
    $output = shell_exec($command);
?>