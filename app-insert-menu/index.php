
<!-- <?php 
    include '../assets/menu.php'
?> -->

<style>
    .row {
        padding-left: 30px;
    }
</style>

<div class="row" style="padding-top: 30px">
    <div class="col-md">
        <h4> INSERT MENU PORTAL </h4>
    </div>
</div>
<form id="inputMenu" action="php/insertMenuBiru.php" method="post" enctype="multipart/form-data" autocomplete="off">
    <div class="row" style="padding-top: 30px">
        <div class="col-md-2">
            Pre-Fix MENU_ID
        </div>
        <div class="col-md-3">
            <input type="text" class="form-control" id="txtMenuId" name="menuId">
        </div>
    </div>

    <div class="row" style="padding-top: 10px">
        <div class="col-md-2">
            Category ID
        </div>
        <div class="col-md-3">
            <select class="form-control" id="cbCategoryId" name="categoryId">
                <?php
                    $command = escapeshellcmd('python python/getCategoryId.py');
                    $output = shell_exec($command);
                
                    echo $output
                ?>
            </select>
        </div>
    </div>

    <div class="row" style="padding-top: 10px">
        <div class="col-md-2">
            Category Group ID
        </div>
        <div class="col-md-3">
            <input type="text" class="form-control" id="txtGroupId" name="groupId">
        </div>
    </div>

    <div class="row" style="padding-top: 10px">
        <div class="col-md-2">
            Process Group Name
        </div>
        <div class="col-md-3">
            <input type="text" class="form-control" id="txtGroupName" name="groupName">
        </div>
    </div>

    <div class="row" style="padding-top: 10px">
        <div class="col-md-2">
            Module Name
        </div>
        <div class="col-md-3">
            <input type="text" class="form-control" id="txtModuleName" name="moduleName">
        </div>
    </div>

    <div class="row" style="padding-top: 10px">
        <div class="col-md-2">
            Menu Name
        </div>
        <div class="col-md-3">
            <input type="text" class="form-control" id="txtMenuName" name="menuName">
        </div>
    </div>

    <div class="row" style="padding-top: 10px">
        <div class="col-md-2">
            Roles Line
        </div>
        <div class="col-md-3">
            <select class="form-control" id="cbRolesLine" name="rolesLine">
                <?php
                    $command = escapeshellcmd('python python/getRolesLine.py');
                    $output = shell_exec($command);
                
                    echo $output
                ?>
            </select>
        </div>
    </div>

    <div class="row" style="padding-top: 10px">
        <div class="col-md-2">
        </div>
        <div class="col-md-1">
            <button type="submit" class="btn btn-block btn-primary" id="btnSave"> Save </button>
        </div>
    </div>
</form>

<div class="row" style="padding: 20px">
    <div class="col-md">
        <table id="table_menu" class="table table-striped table-bordered table-sm" cellspacing="0" width="100%" data-filter-control="true">
            <thead>
                <tr>
                    <th class="th-sm">MENU ID</th>
                    <th class="th-sm">CATEGORY ID</th>
                    <th class="th-sm">CATEGORY GROUP ID</th>
                    <th class="th-sm">ORDERED NUMBER</th>
                    <th class="th-sm">PROCESS GROUP NAME</th>
                    <th class="th-sm">MODULE NAME</th>
                    <th class="th-sm">MENU NAME</th>
                    <th class="th-sm">PATH</th>
                </tr>
            </thead>
            <tbody>
            <?php
                $command = escapeshellcmd('python python/getMenuBiru.py');
                $output = shell_exec($command);
            
                echo $output
            ?>
            </tbody>
            <tfoot>
                <tr>
                    <th class="th-sm">MENU ID</th>
                    <th class="th-sm">CATEGORY ID</th>
                    <th class="th-sm">CATEGORY GROUP ID</th>
                    <th class="th-sm">ORDERED NUMBER</th>
                    <th class="th-sm">PROCESS GROUP NAME</th>
                    <th class="th-sm">MODULE NAME</th>
                    <th class="th-sm">MENU NAME</th>
                    <th class="th-sm">PATH</th>
                </tr>
            </tfoot>
        </table>
    </div>
</div>

<link rel='stylesheet' href='../assets/bootstrap/css/bootstrap.min.css' />
<link rel='stylesheet' href='../assets/css/style.css' />
<link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.10.21/css/dataTables.bootstrap4.min.css"/>

<script src="../assets/js/core/jquery.min.js"></script>
<script src="../assets/js/core/popper.min.js"></script>
<script src="../assets/js/plugins/sweetalert2.js"></script>
<script src="../assets/js/plugins/jquery.dataTables.min.js"></script>
<script type="text/javascript" src="../assets/js/jquery-3.6.0.min.js"></script>
<script type="text/javascript" src="../assets/bootstrap/js/bootstrap.min.js"></script>
<script type="text/javascript" src="https://unpkg.com/sweetalert/dist/sweetalert.min.js"></script>
<script type="text/javascript" src="https://cdn.datatables.net/1.10.21/js/jquery.dataTables.min.js"></script>
<script type="text/javascript" src="https://cdn.datatables.net/1.10.21/js/dataTables.bootstrap4.min.js"></script>

<script type="text/javascript">
    $(document).ready(function () {
        // Setup - add a text input to each footer cell
        $('#table_menu tfoot th').each(function () {
            var title = $(this).text();
            $(this).html('<input type="text" placeholder="Search ' + title + '" />');
        });
        // DataTable
        var table = $('#table_menu').DataTable({
            initComplete: function () {
                // Apply the search
                this.api()
                    .columns()
                    .every(function () {
                        var that = this;
    
                        $('input', this.footer()).on('keyup change clear', function () {
                            if (that.search() !== this.value) {
                                that.search(this.value).draw();
                            }
                        });
                    });
            },
        });

        var r = $('#table_menu tfoot tr');
        r.find('th').each(function(){
            $(this).css('padding', 8);
        });
        $('#table_menu thead').append(r);
        $('#search_0').css('text-align', 'center');

        
    });
</script>

<style>
    tfoot input {
        width: 100%;
        padding: 3px;
        /* box-sizing: border-box; */
        border: none;
        outline: none;
        resize: none;
        background-color: transparent;
    }
</style>