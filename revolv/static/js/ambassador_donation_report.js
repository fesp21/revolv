$(document).ready(function() {
    table = $('#donation_report').DataTable( {
        "processing": true,
        "serverSide": true,
         "dom": 'lfrtBip',
        "scrollX": true,
        buttons: [
             'print',
            {
                extend: 'pdfHtml5',
                orientation: 'landscape',
                pageSize: 'LEGAL'
            },
            {
               extend:    'excelHtml5',
               orientation: 'landscape',
           },
           {
               extend:    'csvHtml5',
               orientation: 'landscape',
           },

        ],
         "order": [[ 4, "desc" ]],
        "ajax": {
         url: '/ambassador_data_table/',
          "data": function ( d ) {
          date1=$('#datepicker-1').val();
          date2=$('#datepicker-2').val();

          d.datepicker1 = date1;
          d.datepicker2 = date2;
        },
         "dataSrc": "data",

        },
        "columns": [
            { "data": "firstname"},
            { "data": "lastname"},
            { "data": "username"},
            { "data": "email"},
            { "data": "date"},
            { "data": "project"},
            { "data": "amount"},
            { "data": "user_reinvestment"},
            { "data": "admin_reinvestment"},
            { "data": "tip"},
            { "data": "total"},
        ],
        "columnDefs": [
        {
            "targets": 8,
            "orderable": false
        },
        {
            "targets":10,
            "orderable": false
        },
        ]

    } );


     $(function() {
            $( "#datepicker-1" ).datepicker({
            dateFormat: 'yy-mm-dd',
            onSelect: function(){}
            }).keyup(function(e) {
            if(e.keyCode == 8 || e.keyCode == 46) {

                if (!$(this).value){
                    $.datepicker._clearDate(this);
                    table.draw();
                }


            }
        });
        $( "#datepicker-2" ).datepicker({
            dateFormat: 'yy-mm-dd',
            onSelect: function(){}
            }).keyup(function(e) {
            if(e.keyCode == 8 || e.keyCode == 46) {

                if (!$(this).value){
                    $.datepicker._clearDate(this);
                }
            }
        });
         });

         $("#search_button").click(function() {
            fromDate=new Date($("#datepicker-1").val());
            toDate=new Date($("#datepicker-2").val());
            if (fromDate!='Invalid Date' && toDate!='Invalid Date')
            {

                if (fromDate.getTime() > toDate.getTime()) {
                    alert("The From date is greater the To date!");
                }else {
                    table.draw();
                }

            }
            else {

                alert('Invalid date');
            }
        });

} );