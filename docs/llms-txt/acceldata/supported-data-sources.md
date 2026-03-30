# Source: https://docs.acceldata.io/documentation/supported-data-sources.md

# Supported Data Sources

Click on an integration card from the list below to navigate to its respective integration page. These are the data sources (integrations) supported by ADOC.

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Acceldata – Published Data Sources</title>
  <style>
    body{font-family:Arial,sans-serif}
    .container{max-width:1200px;margin:0 auto;padding:20px}
    h1{text-align:center;margin-bottom:10px}
    .category-filter{display:flex;justify-content:center;margin-bottom:20px;align-items:center}
    select{padding:8px;font-size:14px}
    .grid-container{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;width:80%;margin:0 auto}
    .grid-item{padding:12px;width:180px;border-radius:8px;background:#fff;box-shadow:rgba(0,0,0,.15) 1.95px 1.95px 2.6px;border:.5px solid darkgray;display:flex;flex-direction:row;transition:transform .3s ease;position:relative;align-items:center;text-decoration:none}
    .grid-item:hover{transform:scale(1.1);cursor:pointer}
    .grid-item img{height:42px;width:42px;background:#fff;border-radius:50%;padding:2px;margin:0 12px 0 4px}
    .grid-itemtext{display:flex;flex-direction:column;font-family:DM Sans, sans-serif}
    .grid-itemtext p{margin:0 0 4px 0;color:#000;font-size:14px}
    .grid-item[data-tooltip]::after{content:attr(data-tooltip);display:none;position:absolute;background:#333;color:#fff;padding:6px 8px;font-size:12px;border-radius:4px;bottom:110%;left:50%;transform:translateX(-50%);z-index:999;white-space:normal;max-width:250px}
    .grid-item[data-tooltip]:hover::after{display:block}
  </style>
</head>
<body>
  <div class="container"><div class="category-filter">
      <label for="categorySelect" style="margin-right:8px;font-weight:bold;">Filter by Category:</label>
      <select id="categorySelect">
        <option value="all" selected>All</option>
        <option value="storage">Storage & Lakes</option>
        <option value="databases">Databases</option>
        <option value="warehouses">Warehouses</option>
      </select>
    </div>

    <div class="grid-container" id="gridContainer"><!-- Data Storage -->
      <a href="https://docs.acceldata.io/documentation/s3" target="_parent" class="grid-item" data-category="storage">
        <img src="https://gitlab.com/naveen55/ad-documentation_assets/-/raw/main/Data%20Source%20Icons/aws_s3.svg" alt="Amazon S3" />
        <div class="grid-itemtext"><p>Amazon S3</p></div>
      </a>
      <a href="https://docs.acceldata.io/documentation/azure-blob-storage" target="_parent" class="grid-item" data-category="storage">
        <img src="https://cdn.prod.website-files.com/64fef88ee8b22d3d21b715a2/66debde9f524e93bd1b63757_Azure%20Blob%20Storage.svg" alt="Azure Blob Storage" />
        <div class="grid-itemtext"><p>Azure Blob Storage</p></div>
      </a>
      <a href="https://docs.acceldata.io/documentation/azure-data-lake-gen2" target="_parent" class="grid-item" data-category="storage">
        <img src="https://cdn.prod.website-files.com/64fef88ee8b22d3d21b715a2/66debd9b35f90cddbe2546c8_Azure%20Data%20Lake%20Gen2.svg" alt="Azure Data Lake Gen2" />
        <div class="grid-itemtext"><p>Azure Data Lake Gen2</p></div>
      </a>
      <a href="https://docs.acceldata.io/documentation/google-cloud-storage" target="_parent" class="grid-item" data-category="storage">
        <img src="https://cdn.prod.website-files.com/64fef88ee8b22d3d21b715a2/66dadc6e0e8f1f59e64e667b_657c72773407a98e92a22fe4_657c06341c2da95ba79ad301_Google%252520Cloud%252520Storage.png" alt="Google Cloud Storage" />
        <div class="grid-itemtext"><p>Google Cloud Storage</p></div>
      </a>
      <a href="https://docs.acceldata.io/documentation/apache-hdfs" target="_parent" class="grid-item" data-category="storage">
        <img src="https://cdn.prod.website-files.com/64fef88ee8b22d3d21b715a2/66dadc693afacf1bcad9113d_657c727846e8fa796febde59_657c05f8d81ab84660268682_HDFS.png" alt="Apache HDFS" />
        <div class="grid-itemtext"><p>Apache HDFS</p></div>
      </a>

      <!-- Databases -->
      <a href="https://docs.acceldata.io/documentation/db2" target="_parent" class="grid-item" data-category="databases">
        <img src="https://cdn.prod.website-files.com/64fef88ee8b22d3d21b715a2/66dadc6e74eaeb4380860243_657c727756c3f5a02b25655e_657c05b92ea0021a9f855e69_DB2.png" alt="IBM DB2" />
        <div class="grid-itemtext"><p>IBM DB2</p></div>
      </a>
      <a href="https://docs.acceldata.io/documentation/mariadb" target="_parent" class="grid-item" data-category="databases">
        <img src="https://cdn.prod.website-files.com/64fef88ee8b22d3d21b715a2/66debac245e36313a716ec51_MariaDB.svg" alt="MariaDB" />
        <div class="grid-itemtext"><p>MariaDB</p></div>
      </a>
      <a href="https://docs.acceldata.io/documentation/azure-mssql" target="_parent" class="grid-item" data-category="databases">
        <img src="https://cdn.prod.website-files.com/64fef88ee8b22d3d21b715a2/66debd7eb2b736c42e37d7e5_Azure%20MSSQL.svg" alt="Azure MSSQL" />
        <div class="grid-itemtext"><p>Azure MSSQL</p></div>
      </a>
      <a href="https://docs.acceldata.io/documentation/postgresql" target="_parent" class="grid-item" data-category="databases">
        <img src="https://cdn.prod.website-files.com/64fef88ee8b22d3d21b715a2/66dadc728b4909b55d3f0b82_657c727a9468cc86e4a3f8d8_657c05cd021f733dd5762f73_PostgreSQL.png" alt="PostgreSQL" />
        <div class="grid-itemtext"><p>PostgreSQL</p></div>
      </a>
      <a href="https://docs.acceldata.io/documentation/amazon-rds-mysql" target="_parent" class="grid-item" data-category="databases">
        <img src="https://cdn.prod.website-files.com/64fef88ee8b22d3d21b715a2/66dadc700e8f1f59e64e69d3_657c7279d5f825e54cd3c9d6_657c05c3a246424009374e40_MySQL.png" alt="Amazon RDS MySQL" />
        <div class="grid-itemtext"><p>Amazon RDS MySQL</p></div>
      </a>
      <a href="https://docs.acceldata.io/documentation/oracle" target="_parent" class="grid-item" data-category="databases">
        <img src="https://cdn.prod.website-files.com/64fef88ee8b22d3d21b715a2/66dadc72b2ea83cc8028f197_657c727aef913a6fb54dd764_657c05af4d04cbf2bea0bdb5_Oracle.png" alt="Oracle" />
        <div class="grid-itemtext"><p>Oracle</p></div>
      </a>
      <a href="https://docs.acceldata.io/documentation/mongodb" target="_parent" class="grid-item" data-category="databases">
        <img src="https://cdn.prod.website-files.com/64fef88ee8b22d3d21b715a2/66dadc703a50df52a952d823_657c72792d59be1c174729e5_657c05988f5d925351dfdeb8_MongoDB.png" alt="MongoDB" />
        <div class="grid-itemtext"><p>MongoDB</p></div>
      </a>
      <a href="https://docs.acceldata.io/documentation/mysql" target="_parent" class="grid-item" data-category="databases">
        <img src="https://gitlab.com/naveen55/ad-documentation_assets/-/raw/main/Data%20Source%20Icons/mysql.svg?ref_type=heads" alt="MySQL" />
        <div class="grid-itemtext"><p>MySQL</p></div>
      </a>

      <a href="https://docs.acceldata.io/documentation/clickhouse" target="_parent" class="grid-item" data-category="databases">
        <img src="https://cdn.prod.website-files.com/64fef88ee8b22d3d21b715a2/66debcf2b6f2832bd137575c_ClickHouse.svg" alt="ClickHouse" />
        <div class="grid-itemtext"><p>ClickHouse</p></div>
      </a>
      <a href="https://docs.acceldata.io/documentation/sap-hana" target="_parent" class="grid-item" data-category="databases">
        <img src="https://cdn.prod.website-files.com/64fef88ee8b22d3d21b715a2/66deba58d8b48d9eb965b6cc_SAP%20Hana.svg" alt="SAP HANA" />
        <div class="grid-itemtext"><p>SAP HANA</p></div>
      </a>
      <!-- <a href="https://docs.acceldata.io/documentation/memsql-singlestoredb" target="_parent" class="grid-item" data-category="databases">
        <img src="https://cdn.prod.website-files.com/64fef88ee8b22d3d21b715a2/66deba18988e68b674baf734_SingleStore.svg" alt="SingleStore" />
        <div class="grid-itemtext"><p>SingleStore</p></div>
      </a> -->
      <a href="https://docs.acceldata.io/documentation/teradata" target="_parent" class="grid-item" data-category="databases">
        <img src="https://cdn.prod.website-files.com/64fef88ee8b22d3d21b715a2/66dadc75f61343c92096471a_657c727b56c3f5a02b256bb3_657c061478f2f8437eae4670_Teradata.png" alt="Teradata" />
        <div class="grid-itemtext"><p>Teradata</p></div>
      </a>

      <!-- Lake/Lakehouses -->
      <a href="https://docs.acceldata.io/documentation/hive" target="_parent" class="grid-item" data-category="storage">
        <img src="https://cdn.prod.website-files.com/64fef88ee8b22d3d21b715a2/66dadc6a94122921f64c6c70_657c7278f8de22914b58ec9f_657c0626011f23acdc7685eb_Hive.png" alt="Apache Hive" />
        <div class="grid-itemtext"><p>Apache Hive</p></div>
      </a>
      <a href="https://docs.acceldata.io/documentation/databricks-integration-for-compute-observability" target="_parent" class="grid-item" data-category="storage">
        <img src="https://cdn.prod.website-files.com/64fef88ee8b22d3d21b715a2/66dadc6d7a2504bd3a104b52_657c727712a6e893de678430_657c066a03cc6ceab49f63ee_databricks.png" alt="Databricks" />
        <div class="grid-itemtext"><p>Databricks</p></div>
      </a><!-- Warehouses -->
      <a href="https://docs.acceldata.io/documentation/aws-athena" target="_parent" class="grid-item" data-category="warehouses">
        <img src="https://cdn.prod.website-files.com/64fef88ee8b22d3d21b715a2/66dadc68f61343c920963ec6_657c727776699bbe73500b71_657c065878f2f8437eae69a8_Athena.png" alt="Amazon Athena" />
        <div class="grid-itemtext"><p>Amazon Athena</p></div>
      </a>
      <a href="https://docs.acceldata.io/documentation/redshift" target="_parent" class="grid-item" data-category="warehouses">
        <img src="https://cdn.prod.website-files.com/64fef88ee8b22d3d21b715a2/66dadc69eef2f0d4d4815c18_657c7277f917ef83a31db82a_657c064e1a4b570cad19c964_Amazon%252520Redshift.png" alt="Amazon Redshift" />
        <div class="grid-itemtext"><p>Amazon Redshift</p></div>
      </a>
      <a href="https://docs.acceldata.io/documentation/azure-synapse-analytics" target="_parent" class="grid-item" data-category="warehouses">
        <img src="https://cdn.prod.website-files.com/64fef88ee8b22d3d21b715a2/66ded02549a4c21ae08c009f_Tableau.svg" alt="Azure Synapse" />
        <div class="grid-itemtext"><p>Azure Synapse</p></div>
      </a>
      <a href="https://docs.acceldata.io/documentation/bigquery" target="_parent" class="grid-item" data-category="warehouses">
        <img src="https://cdn.prod.website-files.com/64fef88ee8b22d3d21b715a2/66dadc6e84be87090cbeecb6_657c7277f917ef83a31db858_657c05191f1671c5196e354f_bigquery.png" alt="Google BigQuery" />
        <div class="grid-itemtext"><p>Google BigQuery</p></div>
      </a>
      <a href="https://docs.acceldata.io/documentation/snowflake-reliability" target="_parent" class="grid-item" data-category="warehouses">
        <img src="https://cdn.prod.website-files.com/64fef88ee8b22d3d21b715a2/66dadc743e0e1e6f13f578e2_657c727c6552ef7b02c46805_657c067489cb2cd233d90ec6_snowflake.png" alt="Snowflake" />
        <div class="grid-itemtext"><p>Snowflake</p></div>
      </a>
      <a href="https://docs.acceldata.io/documentation/fivetran" target="_parent" class="grid-item" data-category="">
        <img src="https://gitlab.com/naveen55/ad-documentation_assets/-/raw/main/Data%20Source%20Icons/fivetran.svg" alt="Fivetran" />
        <div class="grid-itemtext"><p>Fivetran</p></div>
      </a>
      <a href="https://docs.acceldata.io/documentation/collibra" target="_parent" class="grid-item" data-category="">
        <img src="https://gitlab.com/naveen55/ad-documentation_assets/-/raw/main/Data%20Source%20Icons/collibra.svg" alt="Fivetran" />
        <div class="grid-itemtext"><p>Collibra</p></div>
      </a>
    </div>
  </div>

  <script>
    const categorySelect=document.getElementById("categorySelect");
    const gridContainer=document.getElementById("gridContainer");
    const allCards=gridContainer.querySelectorAll(".grid-item");
    function filterCards(){
      const selectedCategory=categorySelect.value;
      allCards.forEach((card)=>{
        const categories=card.getAttribute("data-category").split(",").map(c=>c.trim());
        card.style.display=(selectedCategory==="all"||categories.includes(selectedCategory))?"flex":"none";
      });
      requestParentResize();
    }
    function requestParentResize(){
      const newHeight=document.documentElement.scrollHeight;
      window.parent.postMessage({action:"resizeIframe",height:newHeight},"*");
    }
    categorySelect.addEventListener("change",filterCards);
    filterCards();
    function sendHeightToParent(){
      const contentHeight=document.body.scrollHeight;
      window.parent.postMessage({action:"resizeIframe",height:contentHeight},"*");
    }
    window.onload=sendHeightToParent;
    const observer=new MutationObserver(()=>{sendHeightToParent();});
    observer.observe(document.body,{childList:true,subtree:true});
  </script>
</body>
</html>