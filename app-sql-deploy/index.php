























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