USE Ejem01;

CREATE TABLE ganagato (
    NProducto tinyint NOT NULL,
    Concurso int AUTO_INCREMENT PRIMARY KEY,
    F1 tinyint NOT NULL,
    F2 tinyint NOT NULL,
    F3 tinyint NOT NULL,
    F4 tinyint NOT NULL,
    F5 tinyint NOT NULL,
    F6 tinyint NOT NULL,
    F7 tinyint NOT NULL,
    F8 tinyint NOT NULL,
    Bolsa decimal(13,4) NOT NULL,
    Fecha datetime NOT NULL
)ENGINE=InnoDB;
