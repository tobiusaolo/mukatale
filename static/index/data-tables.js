$(function(){$("#data-table-simple").DataTable({responsive:!0});$("#data-table-row-grouping").DataTable({responsive:!0,columnDefs:[{visible:!1,targets:2}],order:[[2,"asc"]],displayLength:25,drawCallback:function(e){var t=this.api(),l=t.rows({page:"current"}).nodes(),c=null;t.column(2,{page:"current"}).data().each(function(e,t){c!==e&&($(l).eq(t).before('<tr class="group"><td colspan="5">'+e+"</td></tr>"),c=e)})}});$("#page-length-option").DataTable({responsive:!0,lengthMenu:[[10,25,50,-1],[10,25,50,"All"]]}),$("#scroll-dynamic").DataTable({responsive:!0,scrollY:"50vh",scrollCollapse:!0,paging:!1}),$("#scroll-vert-hor").DataTable({scrollY:200,scrollX:!0}),$("#multi-select").DataTable({responsive:!0,paging:!0,ordering:!1,info:!1,columnDefs:[{visible:!1,targets:2}]})}),$(window).on("load",function(){$(".dropdown-content.select-dropdown li").on("click",function(){var e=this;setTimeout(function(){$(e).parent().parent().find(".select-dropdown").hasClass("active")&&($(e).parent().parent().find(".select-dropdown").removeClass("active"),$(e).parent().hide())},100)})});var checkbox=$("#multi-select tbody tr th input"),selectAll=$("#multi-select .select-all");$(document).ready(function(){checkbox.on("click",function(){$(this).parent().parent().parent().toggleClass("selected")}),checkbox.on("click",function(){$(this).attr("checked")?$(this).attr("checked",!1):$(this).attr("checked",!0)}),selectAll.on("click",function(){$(this).toggleClass("clicked"),selectAll.hasClass("clicked")?$("#multi-select tbody tr").addClass("selected"):$("#multi-select tbody tr").removeClass("selected"),$("#multi-select tbody tr").hasClass("selected")?checkbox.prop("checked",!0):checkbox.prop("checked",!1)})});