use segurancaplus

db.createCollection('registro',{
    validator:{
        $jsonSchema:{
            bsonType: 'object',
            required:['nome','sobrenome','CPF','data_registro','descricao'],
            properties: {
                
                nome:{
                    bsonType:'string',
                    maxLength:20
                },
                sobrenome: {
                    bsonType: 'string',
                    maxLength:30
                },
                CPF:{
                    bsonType:'string',
                    minLength:11,
                },
                data_registro:{
                    bsonType:'string'
                },
                descricao:{
                    bsonType:'string',
                    maxLength:500
                }
            }
        }
    }
})